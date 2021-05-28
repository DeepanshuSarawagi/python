from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Walk for 30 minutes a day",
    "february": "Learn Django for 20 minutes a day",
    "march": "Do yoga to correct your spine posture",
    "april": "Walk for 30 minutes a day",
    "may": "Learn Django for 20 minutes a day",
    "june": "Do yoga to correct your spine posture",
    "july": "Walk for 30 minutes a day",
    "august": "Learn Django for 20 minutes a day",
    "september": "Do yoga to correct your spine posture",
    "october": "Walk for 30 minutes a day",
    "november": "Learn Django for 20 minutes a day",
    "december": "Do yoga to correct your spine posture",
}

# Create your views here.

# Remember that every view is a standalone function/class


# def index(request):
#     return HttpResponse("This Works!")  # Created a function which will return the response to a request
#
#
# def feb_index(request):
#     return HttpResponse("This is a response for February index")  # Created a fn/view which will return the response
# # for a request if URI is /challenges/february/
#
#
# def march(request):
#     return HttpResponse("learn a new skill/programming language for 20 minutes every day")

# Commenting the above code briefly so that we can create dynamic views

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month does not exist!")


def monthly_challenge_by_num(request, month):
    return HttpResponse(month)
