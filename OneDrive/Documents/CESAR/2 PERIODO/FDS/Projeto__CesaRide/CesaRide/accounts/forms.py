from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nome de Usuário',required=True, help_text='Requerido: <ul><li>150 caracteres ou menos</li><li>Letras, dígitos e @/./+/-/_ apenas.</li></ul>')

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput,help_text='<ul><li>Sua senha não pode ser muito semelhante às suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul>')

    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    email = forms.EmailField(label='Email')

    phone_number = forms.CharField(label='Número de Telefone', max_length=15, required=True)

    is_student = forms.BooleanField(label='É Estudante?', required=True)

    is_colaborador = forms.BooleanField(label='É Colaborador?', required=False)

    car_model = forms.CharField(label='Modelo do Carro', max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2', 'phone_number','car_model', 'is_student', 'is_colaborador')

