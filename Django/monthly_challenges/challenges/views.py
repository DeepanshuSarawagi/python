from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        response_data = "<h1>{}</h1>".format(challenge_text)
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month does not exist!")


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]  # We are getting the month as an integer argument and getting the actual month
    # from the dictionary using the key. This key is got from the list months by accessing month argument as index
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # Reverse function allows us to construct paths by referring to the name values of URLS
    # in app specific urls.py. It will then prefix the path with URI in the project specific urls.py which is
    # /challenges/
    # It also accepts one more args as array which we want to append after /challenges/ and that is passed as array
    # hence the final result would be challenges/ + redirect_month e.g., /challenges/january
    return HttpResponseRedirect(redirect_path)
