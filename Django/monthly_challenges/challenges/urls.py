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

    # We can also create a placeholder which will be a dynamic identifier. Based on the datatype of URI/placeholder,
    # views will then pass it as an argument and request a function
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_num),

    path("<str:month>", views.monthly_challenge, name="month-challenge")
    # Here month is the placeholder and the syntax to create is <>
    # Here datatype of month is passed as string.
    # Since we have hardcoded the /challenges path in the project specific urls.py, if we make any change there, we need
    # to ensure that similar path change needs to be done app level urls.py as well. To avoid this mistake, we can have
    # Django construct the URL Path for us without hardcoding it in our app specific urls.py or app specific views.py.
    # To make this even more dynamic and have Django construct path so that
    # we dont have to hardcode the path in HTTPResponse, it accepts one more named argument called "name"
    # We set this name parameter to a string value of our choice
    # This named argument is a string and it can be used as a parameter in the reverse function.


]
