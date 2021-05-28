from django.urls import path
from . import views

urlpatterns = [
    path("january", views.index),  # Created a URL pattern. Whenever we hit the /challenges/january URI, Django will
    # call the index function from views
    path("february", views.feb_index)  # Created a URL pattern. Whenever we hit the /challenges/february URI,
    # Django will call the index function from views
]
