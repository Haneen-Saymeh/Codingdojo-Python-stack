from django.shortcuts import render, redirect
from .models import *
from user.models import *



def welcomewall(request):
    context={
        'messages': Message.objects.all().order_by("-created_at"),
        'comments': Comment.objects.all().order_by("created_at"),
        'users'  : User.objects.all()
    }
    if 'userid'  in request.session and  'firstname'  in request.session:
        return render(request,'wall.html', context)
    else:
        return redirect('/user')
    

def addmessage(request):
    user_of = User.objects.get(id=request.session['userid'])
    Message.objects.create(message= request.POST['message'], user=user_of)

 

    return redirect('/wall/welcomewall')


def addcomment(request,id):
    user_of2 = User.objects.get(id=request.session['userid'])
    message_of=Message.objects.get(id= int(id))
    Comment.objects.create(comment= request.POST['comment'], user=user_of2, message=message_of)

 

    return redirect('/wall/welcomewall')


def delmsg(request):
    
    messagedel= Message.objects.get(id=request.POST["message_id"])
    messagedel.delete()
    return redirect('/wall/welcomewall')
