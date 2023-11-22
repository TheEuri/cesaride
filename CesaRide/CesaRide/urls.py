"""
URL configuration for CesaRide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='login'),
    path('signup/',views.signup,name='signup'),
    path('choose_role/',views.choose_role, name='choose_role'),
    path('home/', views.HomePage,name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('passanger_home/',views.passenger_home,name='pagina_passageiro'),
    path('driver_home', views.driver_home, name='pagina_motorista'),
    path('driver/cars/create/', views.car_create, name='car_create'),
    path('driver/cars/', views.car_list, name='car_list'),
    path('driver/create_ride', views.ride_create, name='ride_create'),
    # path('aceitar_corrida/<int:ride_id>/', views.aceitar_corrida, name='aceitar_corrida'),
    path('passenger/request_ride/<int:ride_id>/', views.request_participation_on_ride, name='request_ride'),
    path('detalhes_corrida/<int:ride_id>/', views.detalhes_corrida, name='detalhes_corrida'),
    path('driver/ride/<int:ride_id>/', views.driver_ride_details, name='driver_ride_details'),
    path('driver/ride/<int:ride_id>/update_request/<int:request_id>/<int:status>', views.update_request, name='update_request'),
    path('driver/ride/<int:ride_id>/finish_ride', views.finish_ride, name='finish_ride'),
    path('driver/ride/<int:ride_id>/cancel_ride', views.ride_cancel, name='cancel_ride'),
    path('ride_history/', views.ride_history, name='ride_history'),
]