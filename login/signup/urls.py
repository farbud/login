
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('my_login',views.my_login,name='my_login'),
    path('dashboard',views.dashboard,name='dashboard'),
]