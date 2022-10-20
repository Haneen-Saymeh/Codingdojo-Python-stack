from multiprocessing import context
from django.shortcuts import render, redirect
from .models import User

def regForm(request):
    return render(request,'index.html')


def handle(request):
    User.objects.create(first_name=request.POST['firstName'], last_name=request.POST['lastName'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/show')

def showForm(request):
   

    context={
        'users': User.objects.all()

    }
    return render(request, 'show.html', context)


