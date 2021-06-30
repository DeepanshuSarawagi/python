from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from django.views import View
from .models import Review

# Create your views here.


class ReviewView(View):

    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", context={
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the data to the Review Model db since we have connected the ModelForm with
            # Review model.
            redirect_path = reverse("thankyou")
            return HttpResponseRedirect(redirect_path)
        return render(request, "reviews/review.html", context={
            "form": form
        })


# def review(request):
#     # if request.method == "POST":
#     #     entered_username = request.POST['username']
#     #     if entered_username == "":
#     #         return render(request, "reviews/review.html", context={
#     #             "has_error": True
#     #         })
#     #     print(entered_username)
#     #     redirect_path = reverse("thankyou")
#     #     return HttpResponseRedirect(redirect_path)
#     # Commenting out above code, since we have created a Django Form class
#     # We will handle form specific operations/validations using it
#
#     if request.method == "POST":
#         # existing_data = Re
#         # view.objects.get(pk=1)  # We are getting an existing data and modifying it
#         # form = ReviewForm(request.POST, instance=existing_data)  # This updates the existing data
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'],
#             #                 rating=form.cleaned_data['rating'])
#             # review.save()
#
#             # Commented above code, since we have created a ModelForm instead of a regular Form. We can then directly
#             # call the .save() method on the ReviewForm instance. We need not create a Model instance and then save
#             the
#             # data. Note that, this will save only the new data created by the model. But we can also update the
#             # existing data. We can create an instance of existing model and pass it as a value to the argument
#             # "instance" to the ModelForm object
#
#             form.save()  # This will save the data to the Review Model db since we have connected the ModelForm with
#             # Review model.
#             redirect_path = reverse("thankyou")
#             return HttpResponseRedirect(redirect_path)
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html", context={
#         "form": form
#     })
# Commented out above code since we have created class based view instead of function based view

def thank_you(request):
    return render(request, "reviews/thank_you.html")