from django.urls import path 
from . import views 

app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='my_index'), 
    path('/new', views.new, name='my_new')
]