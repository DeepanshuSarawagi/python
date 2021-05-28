from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),  # Created a URL pattern. Whenever we hit the /challenges/january URI, Django will
    # call the index function from views
    # path("february", views.feb_index), # Created a URL pattern. Whenever we hit the /challenges/february URI,
    # Django will call the index function from views
    # path("march", views.march)
    # Instead of created urlpatterns for every URI, we can create a dynamic placeholder based on the URI accessed by the
    # user. Django will then pass this placeholder as an argument to the views. Views will take this argument and send
    # back the response to the user based on the function/login created
    path("<month>", views.monthly_challenges)  # Here month is the placeholder and the syntax to create is <>
]
