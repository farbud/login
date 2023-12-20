from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'signup/index.html')


def register(request):
    return render(request, 'signup/register.html')


def my_login(request):
    return render(request, 'signup/my_login.html')



def dashboard(request):
    return render(request, 'signup/dashboard.html')
