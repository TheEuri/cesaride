from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Car


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

class LoginForm(forms.Form):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)


class CarForm(forms.ModelForm):
  class Meta:
      model = Car
      fields = ('brand', 'model', 'plate', 'observations')

  def clean_brand(self):
      brand = self.cleaned_data['brand']
      if not brand:
          raise forms.ValidationError('Este campo é obrigatório.')
      return brand

  def clean_model(self):
      model = self.cleaned_data['model']
      if not model:
          raise forms.ValidationError('Este campo é obrigatório.')
      return model

  def clean_plate(self):
      plate = self.cleaned_data['plate']
      if len(plate) > 7:
          raise forms.ValidationError('A placa deve ter no máximo 7 caracteres.')
      return plate

  def clean_observations(self):
      observations = self.cleaned_data['observations']
      if len(observations) > 100:
          raise forms.ValidationError('As observações devem ter no máximo 100 caracteres.')
      return observations
  
class RatingForm (forms.Form):
    rating = forms.IntegerField(min_value = 1, max_value = 5)

