from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.


def review(request):
    # if request.method == "POST":
    #     entered_username = request.POST['username']
    #     if entered_username == "":
    #         return render(request, "reviews/review.html", context={
    #             "has_error": True
    #         })
    #     print(entered_username)
    #     redirect_path = reverse("thankyou")
    #     return HttpResponseRedirect(redirect_path)
    # Commenting out above code, since we have created a Django Form class
    # We will handle form specific operations/validations using it

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            redirect_path = reverse("thankyou")
            return HttpResponseRedirect(redirect_path)
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", context={
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")