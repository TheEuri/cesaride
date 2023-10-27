from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm, LoginForm, CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Car, Ride


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

            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'registro/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('choose_role')
        else:
            return HttpResponse("Nome de Usuário ou Senha incorretos!")
    return render(request, 'registro/signin.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def driver_home(request):
    username = request.user.username
    username = username.capitalize()
    cars = Car.objects.filter(user=request.user)
    rides = Ride.objects.filter(driver=request.user, status='active')
    return render(request, 'registro/driver_home.html', {'username': username, 'cars': cars, 'rides': rides})


def passenger_home(request):
    username = request.user.username
    username = username.capitalize()
    return render(request, 'registro/passenger_home.html', {'username': username})


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


def ride_create(request):
    if request.method == 'POST':
        car = request.POST.get('car')
        max_passengers = request.POST.get('passengers')
        time = request.POST.get('time')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        observations = request.POST.get('observations')
        passenger_price = request.POST.get('price')

        print(car, max_passengers, time, origin, destination, observations, passenger_price)

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


def car_list(request):
    username = request.user.username
    username = username.capitalize()
    cars = Car.objects.filter(user=request.user)
    return render(request, 'car_list.html', {'username': username, 'cars': cars})
