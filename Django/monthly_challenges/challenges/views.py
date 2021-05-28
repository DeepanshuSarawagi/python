from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Remember that every view is a standalone function/class


def index(request):
    return HttpResponse("This Works!")  # Created a function which will return the response to a request


def feb_index(request):
    return HttpResponse("This is a response for February index")  # Created a fn/view which will return the response
# for a request if URI is /challenges/february/


def march(request):
    return HttpResponse("learn a new skill/programming language for 20 minutes every day")

