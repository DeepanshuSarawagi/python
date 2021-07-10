from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view(), name="thankyou"),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    # path("reviews/<int:id>", views.SingleReviewView.as_view())
    path("reviews/<int:pk>", views.SingleReviewView.as_view())  # use the pk for for fetching the data from the Model
    # for the DetailView
]
