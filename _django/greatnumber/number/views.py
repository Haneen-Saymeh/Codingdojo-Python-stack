from django.shortcuts import render, redirect, HttpResponse
import random
from django.utils.datastructures import MultiValueDictKeyError


def pick(request):
    if 'Gnumber' not in request.session:
        request.session['Gnumber']=random.randint(1, 101)
        request.session['status']= ''

    context={
        'status':request.session['status'],
        'number2':request.session['Gnumber'],

    }
    return render(request,'index.html',context)


def process(request):
    number = request.POST['inputnumber']
    if int(number)>request.session['Gnumber']:
        request.session['status'] = "Too high!"

    elif int(number)<request.session['Gnumber']:
        request.session['status'] = "Too low!"
       

    elif int(number)==request.session['Gnumber']:
        
        request.session['number']=number
        
        request.session['status'] = "same number!"
        
        
    return redirect('/')



def destroy(request):
    if 'Gnumber' in request.session:
        del request.session['Gnumber']
    return render(request, 'over.html')
    	




