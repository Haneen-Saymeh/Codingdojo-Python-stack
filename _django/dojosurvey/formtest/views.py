from django.shortcuts import render

def showForm(request):
    return render(request,'index.html')

def showInfo(request):
    name_form=request.POST['name']
    select_form=request.POST['select']
    select2_form=request.POST['select2']
    comment_form=request.POST['comment']

    context={
        "name":name_form,
        "select1":select_form ,
        "select2":select2_form,
        "comment":comment_form
    }
    return render(request, "info.html",context)