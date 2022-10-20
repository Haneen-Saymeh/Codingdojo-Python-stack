from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


def fatima(request):
    return HttpResponse("hiiii")
def root(request):
    return redirect ("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to  display a new form to create a new blog")


def create(request):
    return redirect ('/')

def show(request,val):
    return HttpResponse(f'placeholder to  display a blog number {val}.')


def edit(request,val):
    return HttpResponse(f'placeholder to  edit blog number {val}.')

def destroy(request,val):
    return redirect ('/blogs')


def lastone(request):
    context={
        "title": "my first blog",
        "content":"this blog is about something"
    }
    return JsonResponse(context)