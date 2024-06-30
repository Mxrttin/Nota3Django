from django.urls import path 
from. import views
from .views import  register , exit


urlpatterns = [
    path('inicioS',views.login , name="inicioS"),
    path('register/', register, name='register'),
    path('logout/',exit, name = 'exit'),


]
