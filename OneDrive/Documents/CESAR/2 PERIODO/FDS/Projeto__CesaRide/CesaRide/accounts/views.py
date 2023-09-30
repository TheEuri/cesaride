from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')



def HomePage (request):
    if request.user.role == 'DR':
        return render(request, 'registro/home.html')
    elif request.user.role == 'PS':
        return render(request,'registro/passenger_home.html')
    else:
        return HttpResponse("Role not defined!")

def signup(request):
    User = get_user_model()
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if User.objects.filter(username=username):
            return HttpResponse("Usuário já existe! Por favor, tentre outro nome")
        
        if User.objects.filter(email=email):
            return HttpResponse("Email já registrado!")
        
        if len(username) > 20:
            return HttpResponse("Nome de usuário deve ser até no máximo 20 caracteres")
        
        if not username.isalnum():
            return HttpResponse("Nome de usuário deve ser alfanumérico!")

        if pass1!=pass2:
            return HttpResponse("Sua senha e confirmação de senha não são iguais!")
        else:

            my_user= User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('choose_role')
        



    return render (request,'registro/signup.html')




def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('choose_role')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'registro/signin.html')


def LogoutPage (request):
    logout(request)
    return redirect ('login')


def driver_home (request):
    #inserir codigo
    return render(request, 'registro/driver_home.html')


def passenger_home (request):
    return render (request,'registro/passenger_home.html')

def choose_role(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            role = form.cleaned_data.get('role')
            request.user.role = role
            request.user.save()
            print("Papel escolhido: ",role)

            if role == 'DR':
                return redirect('pagina_motorista')
            
            elif role == 'PS':
                return redirect('pagina_passageiro')
            
    else:
        form = LoginForm()
    return render (request, 'registro/choose_role.html', {'form':form})



