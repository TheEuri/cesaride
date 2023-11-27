from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm, LoginForm, CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Car, LostItemRequest, Ride, RequestParticipationInRide, RideReview
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    if request.user.role == 'DR':
        return render(request, 'registro/home.html')
    elif request.user.role == 'PS':
        return render(request, 'registro/passenger_home.html')
    else:
        return HttpResponse("Role not defined!")


def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')

        print(username, email, pass1, pass2, phone_number)

        if User.objects.filter(username=username):
            return HttpResponse("Usuário já existe! Por favor, tentre outro nome")

        if User.objects.filter(email=email):
            return HttpResponse("Email já registrado!")

        if len(username) > 20:
            return HttpResponse("Nome de usuário deve ser até no máximo 20 caracteres")

        if not username.isalnum():
            return HttpResponse("Nome de usuário deve ser alfanumérico!")

        if pass1 != pass2:
            return HttpResponse("Sua senha e confirmação de senha não são iguais!")
        else:

            my_user = User.objects.create_user(username=username, email=email, password=pass1, phone_number=phone_number)
            my_user.save()
            print("Usuário criado com sucesso!")
            return redirect('login')

    return render(request, 'registro/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            print("Usuário logado com sucesso!")
            return redirect('choose_role')
        else:
            return HttpResponse("Nome de Usuário ou Senha incorretos!")
    return render(request, 'registro/signin.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def driver_home(request):
  username = request.user.username
  username = username.capitalize()
  cars = Car.objects.filter(user=request.user)
  rides = Ride.objects.filter(driver=request.user, status='active')
  lost_items = LostItemRequest.objects.filter(ride__driver=request.user)
  return render(request, 'registro/driver_home.html', {'username': username, 'cars': cars, 'rides': rides, 'lost_items': lost_items})


@login_required(login_url='login')
def passenger_home(request):
  username = request.user.username
  username = username.capitalize()
  rides = Ride.objects.filter(status='active').exclude(driver=request.user).order_by('time')
  requests = RequestParticipationInRide.objects.filter(passenger=request.user)
  for ride in rides:
    for requestPart in requests:
      if ride.id == requestPart.ride.id:
        ride.requestStatus = requestPart.status

        print(ride)
        break

    
  return render(request, 'registro/passenger_home.html', {'username': username, 'rides': rides})


@login_required(login_url='login')
def choose_role(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            role = form.cleaned_data.get('role')
            request.user.role = role
            request.user.save()
            print("Papel escolhido: ", role)

            if role == 'DR':
                return redirect('pagina_motorista')

            elif role == 'PS':
                return redirect('pagina_passageiro')

    else:
        form = LoginForm()
    return render(request, 'registro/choose_role.html', {'form': form})


@login_required(login_url='login')
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # Salvar o carro e redirecionar para a página de detalhes
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('pagina_motorista')
    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})


@login_required(login_url='login')
def ride_create(request):
    if request.method == 'POST':
        car = request.POST.get('car')
        max_passengers = request.POST.get('passengers')
        time = request.POST.get('time')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        observations = request.POST.get('observations')
        passenger_price = request.POST.get('price')

        print(car, max_passengers, time, origin,
              destination, observations, passenger_price)

        if car and max_passengers and time and origin and destination and passenger_price and float(passenger_price) < 999.00 and float(passenger_price) > 0:
            ride = Ride.objects.create(driver=request.user, max_passengers=max_passengers, time=time, origin=origin,
                                       destination=destination, observations=observations, passenger_price=passenger_price, car=Car.objects.get(id=car))
            ride.save()

            print(ride)
            return redirect('pagina_motorista')
        else:
            return HttpResponse("Preencha todos os campos corretamente!")
    else:
        cars = Car.objects.filter(user=request.user)
        context = {'cars': cars}
        return render(request, 'create_ride.html', context)


@login_required(login_url='login')
def car_list(request):
    username = request.user.username
    username = username.capitalize()
    cars = Car.objects.filter(user=request.user)
    return render(request, 'car_list.html', {'username': username, 'cars': cars})


# @login_required(login_url='login')
# def aceitar_corrida(request, ride_id):
#     ride = get_object_or_404(Ride, id=ride_id)
#     if ride.passengers.count() < ride.max_passengers:
#         ride.passengers.add(request.user)
#         ride.save()

#         return redirect('detalhes_corrida', ride_id=ride_id)
#     else:
#         return HttpResponse("Desculpe, esta corrida já atingiu o número máximo de passageiros.")

@login_required(login_url='login')
def request_participation_on_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if request.method == 'POST':
      if ride.passengers.count() >= ride.max_passengers:
        return HttpResponse("Desculpe, esta corrida já atingiu o número máximo de passageiros.")
      else:
        if (RequestParticipationInRide.objects.filter(ride=ride, passenger=request.user).exists()):
          return HttpResponse("Você já solicitou participação nesta corrida!")
        else:
          origin = request.POST.get('origin')
          destination = request.POST.get('destination')
          if origin and destination:
            request_participation = RequestParticipationInRide.objects.create(ride=ride, passenger=request.user, origin=origin, destination=destination)
            request_participation.save()
            return redirect('detalhes_corrida', ride_id=ride_id)
          else:
            return HttpResponse("Preencha todos os campos corretamente!")
    else:
      if (RequestParticipationInRide.objects.filter(ride=ride, passenger=request.user).exists()):
          return redirect('detalhes_corrida', ride_id=ride_id)
      else:
        return render(request, 'request_ride.html', {'ride': ride})

@login_required(login_url='login')
def detalhes_corrida(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    requestStatus = RequestParticipationInRide.objects.filter(ride=ride, passenger=request.user)[0]
    username = request.user.username
    username = username.capitalize()

    return render(request, 'detalhes.html', {'username': username, 'ride': ride, 'requestStatus': requestStatus})

@login_required(login_url='login')
def driver_ride_details(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    username = request.user.username
    username = username.capitalize()

    requests = RequestParticipationInRide.objects.filter(ride=ride, status='pending')

    return render(request, 'driver_ride_details.html', {'username': username, 'ride': ride, 'requests': requests})

@login_required(login_url='login')
def update_request(request, ride_id, request_id, status):
    ride = get_object_or_404(Ride, id=ride_id, driver=request.user)
    requestPart = get_object_or_404(RequestParticipationInRide, id=request_id, ride=ride)

    if status == 1:
      requestPart.status = 'accepted'
      requestPart.save()
      ride.passengers.add(requestPart.passenger)
      ride.save()
    elif status == 0:
      requestPart.status = 'rejected'
      requestPart.save()

    return redirect('driver_ride_details', ride_id=ride_id)

@login_required(login_url='login')
def finish_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id, driver=request.user)
    
    if request.method == 'GET':
        ride.status = 'finished'
        ride.rating = request.POST.get('rating')
        ride.save()
        return redirect('pagina_motorista')
    
    return render(request, 'finish_ride.html', {'ride': ride})

@login_required(login_url='login')
def ride_history(request):
  username = request.user.username
  username = username.capitalize()
  rides = Ride.objects.filter(Q(driver=request.user) | Q(passengers=request.user), status__in=['finished', 'cancelled']).distinct()
  reviews = RideReview.objects.filter(ride__in=rides)
  return render(request, 'ride_history.html', {'username': username, 'rides': rides, 'reviews': reviews})

@login_required(login_url='login')
def ride_cancel(request, ride_id):
  ride = get_object_or_404(Ride, id=ride_id)
  if request.user == ride.driver:
    ride.status = 'cancelled'
    ride.save()
    return redirect('pagina_motorista')
  else:
    requestPart = get_object_or_404(RequestParticipationInRide, ride=ride, passenger=request.user)
    requestPart.status = 'cancelled'
    requestPart.save()
    return redirect('pagina_passageiro')

@login_required(login_url='login')
def request_lost_item(request, ride_id):
  ride = get_object_or_404(Ride, id=ride_id)
  if request.method == 'GET':
    return render(request, 'request_lost_item.html', {'ride': ride})
  if request.method == 'POST':
    item_name = request.POST.get('item')
    item_description = request.POST.get('description')
    if item_name and item_description:
      if ride.status == 'finished':
        request_lost_item = LostItemRequest.objects.create(ride=ride, passenger=request.user, item_name=item_name, item_description=item_description)
        request_lost_item.save()
        return redirect('pagina_passageiro')
      else:
        return HttpResponse("Você só pode solicitar itens perdidos de corridas finalizadas!")
    else:
      return HttpResponse("Preencha todos os campos corretamente!")

@login_required(login_url='login')
def lost_items(request):
  username = request.user.username
  username = username.capitalize()
  lost_items = LostItemRequest.objects.filter(ride__driver=request.user)
  return render(request, 'lost_items.html', {'username': username, 'lost_items': lost_items})

@login_required(login_url='login')
def rate_ride(request, ride_id):
  ride = get_object_or_404(Ride, id=ride_id)
  if request.method == 'GET':
    return render(request, 'review_driver.html', {'ride': ride})
  if request.method == 'POST':
    rating = request.POST.get('rate')
    review = request.POST.get('description')
    if rating:
      if ride.status == 'finished':
        review_driver = RideReview.objects.create(ride=ride, passenger=request.user, rating=rating, review=review)
        review_driver.save()
        return redirect('pagina_passageiro')
      else:
        return HttpResponse("Você só pode avaliar motoristas de corridas finalizadas!")
    else:
      return HttpResponse("Preencha todos os campos corretamente!")
    
@login_required(login_url='login')
def view_rate(request):
  username = request.user.username
  username = username.capitalize()
  reviews = RideReview.objects.filter(ride__driver=request.user)
  return render(request, 'driver_rate.html', {'username': username, 'reviews': reviews})