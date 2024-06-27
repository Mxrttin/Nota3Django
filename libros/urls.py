from django.urls import path 
from. import views

urlpatterns = [
    path('comics',views.comics , name="comics"),
    path('mangas',views.mangas , name="mangas"),
    path('destacados',views.destacados , name="destacados"),

]
