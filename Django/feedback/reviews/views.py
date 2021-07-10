from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView


# Create your views here.


# class ReviewView(View):
#
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", context={
#             "form": form
#         })
#
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()  # This will save the data to the Review Model db since we have connected the ModelForm with
#             # Review model.
#             redirect_path = reverse("thankyou")
#             return HttpResponseRedirect(redirect_path)
#         return render(request, "reviews/review.html", context={
#             "form": form
#         })


class ReviewView(FormView):
    template_name = "reviews/review.html"
    form_class = ReviewForm  # We need to let Django know which Form class should be used for rendering the template
    # and validating the data. Using FormView, will eliminate the use of  get() method

    # Form submission is also automatically handled by the FormView i.e., POST method
    success_url = "/thank-you"  # We need to define this parameter to let Django know to redirect when the form
    # submission is successful

    def form_valid(self, form):  # We also need to explicitly let Django know to save the data in database when the
        # form submission is successful
        form.save()
        return super(ReviewView, self).form_valid(form)

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


# class ThankYouView(View):
#
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super(ThankYouView, self).get_context_data()
        context['message'] = "This works"  # construct the context which will be exposed to the template
        return context


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(ReviewsListView, self).get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# We have commented out above code because we are going to render the list of data using the ListView template

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"

    model = Review  # Django will now fetch the list of data using the model. Hence, we are pointing the model variable
    # with the actual Model which has data
    # Django will then render the data by the Model which we have pointed to and render it to the template
    # review_list.html
    context_object_name = "reviews"  # This variable will hold the list of model data which will be rendered to the
    # template

    # By overriding below data we are controlling what data should be rendered to the template.
    # Here we are returning data to the template by using the queryset() and filtering data where rating > 4
    def get_queryset(self):
        base_query = super(ReviewsListView, self).get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#
#     def get_context_data(self, **kwargs):
#         # print(kwargs)  # Understand of use of kwargs here
#         context = super(SingleReviewView, self).get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context


# We have commented out above code to learn about DetailView. Whenever we want to return a template with a single piece
# of data we can use the DetailView instead of generic Template View


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review  # Just like in the ListView we need to set the model property with the actual Model from which it
    # has to fetch the data. For fetching the single piece of data from the Model, we need to provide any context since
    # Django will load the data automatically. In the urls.py we need to identify the single piece of data using pk
    # - primary key. Django will then automatically load the data using the pk from the Model and render it in the
    # template

    def get_context_data(self, **kwargs):
        context = super(SingleReviewView, self).get_context_data()
        loaded_review = self.object  # We are loading the review
        request = self.request  # we are getting the request here
        favorite_id = request.session["favorite_review"]  # getting the session's data
        context["is_favorite"] = favorite_id == str(loaded_review.id)  # comparing the ID's and checking if this is
        # favorite review
        return context


class AddFavoriteView(View):

    def post(self, request):
        review_id = request.POST['review_id']
        # fav_review = Review.objects.get(pk=review_id)
        # request.session["favorite_review"] = fav_review  # request has a property called session. We are adding new
        # data to this session by using a key and value of choice. hence we are using a key of favorite_review and
        # storing fav_review as value in it.
        # Now, this line of code will error out since we are saving the Review Object in the session data. And object
        # is not JSON serializable. Instead, we need to save data which either has to be a string or a dictionary.
        # Hence we will comment out this line of code and just save the review_id which is a string data.
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
