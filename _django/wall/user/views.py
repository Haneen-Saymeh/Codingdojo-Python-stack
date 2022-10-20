from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def regpage(request):
    return render(request, 'reg.html')

def regprocess(request):
    errors = User.objects.basic_validator(request.POST)
    users= User.objects.all()
    for user in users:
        if user.email ==request.POST['email']:
            errors['email']= 'This Email already exist in our database!'
        
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/user')

    else:
        
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=firstname, last_name=lastname, email= email,password=pw_hash) 
        request.session['firstname'] = User.objects.last().first_name
        request.session['userid'] = User.objects.last().id
        
        
        messages.success(request, "Registration successfully completed")
        
        return redirect('/wall/welcomewall')

# def welcome(request):
#     if 'userid'  in request.session and  'firstname'  in request.session:
#         return render(request,'welcome.html')
#     else:
#         return redirect('/user')

    


def log(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['firstname'] = logged_user.first_name
            request.session['userid'] = logged_user.id

            messages.success(request, "Login successfully completed")
            return redirect('/wall/welcomewall')
        messages.success(request, "Invalid Credintial!")
        return redirect('/user')
    messages.success(request, "Invalid Credintial!")
    return redirect('/user')


def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
    if 'firstname' in request.session:
        del request.session['firstname']
    
        
    request.session.flush()
    return redirect('/user')
        
        


