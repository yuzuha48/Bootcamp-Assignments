from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.form), 
    path('ninja_gold', views.index),
    path('process_money/<str:location>', views.process_money)
]