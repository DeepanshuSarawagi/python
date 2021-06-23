from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def review(request):
    if request.method == "POST":
        entered_username = request.POST['username']
        print(entered_username)
        redirect_path = reverse("thankyou")
        return HttpResponseRedirect(redirect_path)
    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")