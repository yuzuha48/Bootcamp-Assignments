from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index), 
    path('register', views.register), 
    path('login', views.login),
    path('wall', views.wall), 
    path('post_message', views.post_message), 
    path('comment/<int:message_id>', views.comment), 
    path('destroy/<int:message_id>', views.delete)
]