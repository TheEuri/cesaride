from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Número de telefone do usuário
    phone_number = models.CharField(max_length=15, blank=True)

    # Se o usuário é um estudante ou colaborador da CESAR School
    is_student = models.BooleanField(default=True)

    is_colaborador = models.BooleanField(default=True)

    # O carro que o usuário usa para dar caronas
    car_model = models.CharField(max_length=30, blank=True)
