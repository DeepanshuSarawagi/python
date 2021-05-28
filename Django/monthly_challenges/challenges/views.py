from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Walk for 30 minutes a day"
    elif month == "february":
        challenge_text = "Learn a new programming skill"
    elif month == "march":
        challenge_text = "Meditate for at least 20 minutes a day"
    else:
        return HttpResponseNotFound("Oops! Page not found.")
    return HttpResponse(challenge_text)


def monthly_challenges_by_num(request, month):
    return HttpResponse(month)
