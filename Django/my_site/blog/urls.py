from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
    path("posts", views.all_posts, name="posts-page"),
    path("posts/<slug>", views.post_detail, name="post-detail-page")  # This concept of having URLs like this is
    # called as slug
]
