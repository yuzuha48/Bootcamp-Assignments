from django.urls import path 
from . import views 

urlpatterns = [
    path('/', views.index), 
    path('/create', views.create), 
    path('/view_comments/<int:course_id>', views.view_comments),
    path('/add_comment/<int:course_id>', views.add_comment),
    path('/delete/<int:course_id>', views.delete),
    path('/destroy/<int:course_id>', views.destroy)
]