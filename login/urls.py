from django.urls import path 
from. import views
from .views import  register


urlpatterns = [
    path('inicioS',views.login , name="inicioS"),
    path('register/', register, name='register'),


]
