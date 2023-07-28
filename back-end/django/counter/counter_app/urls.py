from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path("destroy_session", views.destroy),
    path("add_two", views.double),
    path("add_count", views.add_num)
]