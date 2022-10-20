from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *


def showbooks(request):
    context={
        'books': Book.objects.all()
        }
    return render(request, 'book.html', context)



def addbook(request):
    Book.objects.create(title=request.POST['booktitle'], desc= request.POST['desc'])
    return redirect("/")


def viewbook(request,id):
    context={
        "bookone": Book.objects.get(id=id),
        'authors': Author.objects.all()
        }
    return render(request, 'view.html', context)


def authtobook(request,id):
    book1= Book.objects.get(id=int(id))
    author1=Author.objects.get(id=request.POST['selectauthors'])
    book1.authors.add(author1)
    book1.save()

    return redirect("/books/"+str(id))




def showauthors(request):
    context={
        'authors': Author.objects.all()
        }
    return render(request, 'author.html', context)

def addauthor(request):
    Author.objects.create(first_name=request.POST["firstname"],last_name=request.POST["lastname"],notes=request.POST["notes"])
    return redirect("/authors")



def viewauthor(request, id):
    context= {
        "oneauthor": Author.objects.get(id=id),
        'allbooks':Book.objects.all()
    }
    return render(request, 'view2.html', context)

def booktoauth(request,id):
    author_instance=Author.objects.get(id=id)
    book_instance= Book.objects.get(id=request.POST['selectbooks'])
    author_instance.books.add(book_instance)
    author_instance.save()
    return redirect('/authors/'+str(id))


