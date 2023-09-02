from django.urls import path 
from . import views 

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='my_index'),
    path('/new', views.new, name='my_new'), 
    path('/create', views.create, name='my_create'), 
    path('/<int:number>', views.show, name='my_show'), 
    path('/<int:number>/edit', views.edit, name='my_edit'), 
    path('/<int:number>/delete', views.destroy, name='my_destroy'), 
    path('/json', views.json)
]