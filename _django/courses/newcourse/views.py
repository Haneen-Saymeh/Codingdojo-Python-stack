from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def showcourses(request):
    context={
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)


def addcourse(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST["name"], description=request.POST['desc'])
        messages.success(request, "Show successfully Created")
        return redirect('/')


def ConfirmDestroy(request,id):
    context={
        'onecourse': Course.objects.get(id=int(id))
    }
    return render(request,"destroy.html", context)

def destroy(request,id):
    courseone= Course.objects.get(id=int(id))
    courseone.delete()
    return redirect("/")


