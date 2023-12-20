
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('',views.register,name='register'),
    path('',views.my_login,name='my_login'),
    path('',views.dashbord,name='dashbord'),
]