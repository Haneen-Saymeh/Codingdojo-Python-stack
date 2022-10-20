from django.shortcuts import render, redirect
from .models import *

def showForm(request):
    context = {
        "dojos": Dojo.objects.all()

    }

    return render(request,"index.html", context)


def dojo(request):
    Dojo.objects.create(name= request.POST['dojoname'], city=request.POST['dojocity'], state= request.POST['dojostate'])

    return redirect('/')


def ninja(request):
    dojos_of = Dojo.objects.get(id=request.POST['selectdojo'])
    Ninja.objects.create(first_name= request.POST['ninjafirstname'], last_name= request.POST['ninjalastname'], dojo=dojos_of)

    return redirect('/')
