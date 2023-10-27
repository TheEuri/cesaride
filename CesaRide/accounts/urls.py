from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('driver_home/', views.driver_home, name='pagina_motorista'),
    path('passenger_home/', views.passenger_home, name='pagina_passageiro'),
    path('choose_role/', views.choose_role, name='choose_role'),
    path('aceitar_corrida/<int:ride_id>/', views.aceitar_corrida, name='aceitar_corrida'),
    path('detalhes_corrida/<int:ride_id>/', views.detalhes_corrida, name='detalhes_corrida'),
    path('aceitar_solicitacao/<int:request_id>/', views.aceitar_solicitacao, name='aceitar_solicitacao'),
    path('recusar_solicitacao/<int:request_id>/', views.recusar_solicitacao, name='recusar_solicitacao'),
    path('solicitacoes_pendentes/', views.solicitacoes_pendentes, name='solicitacoes_pendentes'),
]
