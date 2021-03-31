from django.shortcuts import render, redirect
from coursesapp.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'all_courses' : Course.objects.all()
    }
    return render (request, 'home.html', context)

def add_course(request): 
    
    errors = Course.objects.basic_validators(request.POST)
    
    if len(errors)>0:
        for k,v in errors.items():
            messages.error(request, v)
        return redirect ('/')
    else:
        name = request.POST['name']
        description = request.POST['desc']
        course = Course.objects.create(name = name)
        Description.objects.create(course = course, description = description)
        return redirect ('/')
        
def show_delete_page(request, course_id):
    course = Course.objects.get(id = course_id)
    context = {
        'course': course
    }
    return render(request, 'delete_page.html', context)

def delete_course(request, course_id):
    course = Course.objects.get(id = course_id)
    course.delete()
    return redirect ('/')