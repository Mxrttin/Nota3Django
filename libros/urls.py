from django.urls import path 
from . import views
from .views import buscar , detalles


urlpatterns = [
    path('comics',views.comics , name="comics"),
    path('buscar/', buscar , name="buscar"),
    path('mangas',views.mangas , name="mangas"),
    path('destacados',views.destacados , name="destacados"),
    path('detalles/', views.detalles, name='detalles'),


]
