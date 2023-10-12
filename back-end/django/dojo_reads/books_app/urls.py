from django.urls import path 
from . import views

urlpatterns = [
    path('', views.view_all),
    path('/add', views.add), 
    path('/create', views.create), 
    path('/create_review', views.create_review), 
    path('/<int:book_id>', views.view), 
    path('/delete/<int:review_id>', views.delete)
]