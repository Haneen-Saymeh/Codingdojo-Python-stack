from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages



def allshows(request):
    context ={
        'shows': Show.objects.all()
    }

    return render(request, "allshows.html", context)



def newshow(request):
    return render(request, "newshow.html")



def createshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST["title"], network=request.POST['network'],release_date=request.POST['date'],description=request.POST['desc'])
        messages.success(request, "Show successfully Created")
        return redirect('/shows')




def showtv(request, id):
    context = {
        "oneshow" : Show.objects.get(id=id)
    }

    return render(request, 'showtv.html', context)



def editshow(request,id):
    context={
        "oneshow" : Show.objects.get(id=id)

    }
    
    return render(request, 'edit.html', context)





def updateshow(request,id):
    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:

        showinstance = Show.objects.get(id=id)
        
        showinstance.title=request.POST["title"]
        showinstance.network=request.POST["network"]
        showinstance.release_date=request.POST["date"]
        showinstance.description=request.POST["desc"]
        showinstance.save()
           
        
        return redirect("/shows")



def deleteshow(request,id):

    instance = Show.objects.get(id=id)
    instance.delete()

    
    return redirect('/shows')



    

    
    






