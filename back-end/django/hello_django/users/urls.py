from django.urls import path 
from . import views

app_name = 'users'

urlpatterns = [
    path('register', views.register, name='my_register'), 
    path('login', views.login, name='my_login'), 
    path('users/new', views.register, name='my_new'), 
    path('users', views.users, name='my_users')
]