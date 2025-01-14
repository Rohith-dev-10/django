# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "complete 20% dsa",
    "february": "complete 40% dsa and 20% development project",
    "march": "complete 60% dsa and 50% development project",
    "april": "complete 240+ dsa questions and deployment of project",
    "may": "do something interesting in life",
    "june": "I'm going to do something awesome",
    "july": "almost ready for interview",
    "august": "now I'm become the death",
    "september": "I am the devil of my world",
    "october": "let's do party after PPO",
    "november": "now it's time to enjoy life",  # Corrected key
    "december": None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html",{
        "months" : months
    })
    
def monthly_challenege_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenges.html", {
            "text" : challenge_text,
            "month_name" : month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>the invalid input plz contact MR.Rohith Uppunuthula</h1>")