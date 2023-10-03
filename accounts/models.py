from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class CustomUser(AbstractUser):
    # Número de telefone do usuário
    phone_number = models.CharField(max_length=15, blank=True)

    # Se o usuário é um estudante ou colaborador da CESAR School
    is_student = models.BooleanField(default=True)

    is_colaborador = models.BooleanField(default=True)

    # O carro que o usuário usa para dar caronas
    car_model = models.CharField(max_length=30, blank=True)

    DRIVER = 'DR'
    PASSENGER = 'PS'
    ROLE_CHOICES = [
        (DRIVER, 'Motorista'),
        (PASSENGER, 'Passageiro'),
    ]
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=PASSENGER,
    )

class LoginForm (forms.Form):
    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)

    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate = models.CharField(max_length=7)
    observations = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)