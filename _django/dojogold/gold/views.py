from django.shortcuts import render, redirect

import random

from time import gmtime, strftime, localtime


def startgame(request):
     if 'gold' not in request.session:
        request.session['gold'] = 0
     if 'activities' not in request.session:
        request.session['activities'] = []
        
     return render(request,'index.html')


def process(request):
    
    if request.POST['which_game'] == 'farm':
        request.session['farmGold'] = random.randint(10, 20)
        request.session['gold'] += request.session['farmGold']
        text_farm = f"You entered a farm and earned {request.session['farmGold']} gold." 
        time_farm= strftime("%Y-%m-%d %H:%M %p", localtime())
        farm=text_farm+time_farm
        request.session['activities'].append(farm)
        request.session.save()
        

  
    elif request.POST['which_game'] == 'cave':
        request.session['caveGold'] = random.randint(10, 20)
        request.session['gold'] += request.session['caveGold']
        text_cave = f"You entered a cave and earned {request.session['caveGold']} gold." 
        time_cave= strftime("%Y-%m-%d %H:%M %p", localtime())
        cave= text_cave+time_cave
        request.session['activities'].append(cave)
        request.session.save()
        
        

    elif request.POST['which_game'] == 'house':
        request.session['houseGold'] = random.randint(10, 20)
        request.session['gold'] += request.session['houseGold']
        text_house = f"You entered a house and earned {request.session['houseGold']} gold." 
        time_house= strftime("%Y-%m-%d %H:%M %p", localtime())
        house= text_house+time_house
        request.session['activities'].append(house)
        request.session.save()
        
        

    elif request.POST['which_game'] == 'quest':
        request.session['questGold'] = random.randint(-50, 50)
        if request.session['questGold'] > 0:
            request.session['gold'] += request.session['questGold']
            text_quest= f"You completed a quest and earned {request.session['questGold']} gold." 
            time_quest= strftime("%Y-%m-%d %H:%M %p", localtime())
            quest= text_quest+time_quest
            request.session['activities'].append(quest)
            request.session.save()
        else:
            request.session['gold'] =   request.session['gold']  + request.session['questGold']
            text_quest= f"You failed a quest and lost {request.session['questGold']} gold. Ouch!" 
            time_quest= strftime("%Y-%m-%d %H:%M %p", localtime())
            quest= text_quest+time_quest
            request.session['activities'].append(quest)
            request.session.save()

        

    return redirect('/')
       

def reset(request):
    if 'gold' in request.session:
        del request.session['gold']
    if 'activities' in request.session:
        del request.session['activities']
    return redirect('/')

      
