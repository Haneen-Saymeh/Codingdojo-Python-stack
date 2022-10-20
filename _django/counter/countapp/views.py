from django.shortcuts import render, redirect

def showCounter(request):
    if 'hanin' not in request.session:
        request.session['hanin'] =1
    else:
        request.session['hanin'] +=1

    return render(request, 'index.html')


def destroy(request):
    del request.session['hanin']

    return redirect('/')	

