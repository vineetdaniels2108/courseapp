from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('course/add_course', views.add_course), 
    path('course/<int:course_id>', views.show_delete_page), 
    path('course/<int:course_id>/destroy', views.delete_course),
]
