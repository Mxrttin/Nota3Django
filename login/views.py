from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def login(request):
    context = {}
    return render(request , "login/inicioS.html",context)