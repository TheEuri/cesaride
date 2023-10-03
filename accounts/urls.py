from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin, name='signin'),
    path('driver_home/', views.driver_home,name='pagina_motorista'),
    path('passenger_home/',views.passenger_home,name='pagina_passageiro'),
    path('choose_role/',views.choose_role,name='choose_role'),
]