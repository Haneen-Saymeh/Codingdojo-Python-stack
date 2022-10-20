from django.shortcuts import render

def showgame(request):

    return render(request, 'game.html')
