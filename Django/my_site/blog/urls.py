from django.urls import path

urlpatterns = [
    path(""),
    path("posts"),
    path("posts/<slug>")  # This concept of having URLs like this is called as slug
]
