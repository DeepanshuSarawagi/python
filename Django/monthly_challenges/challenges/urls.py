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
    path("<int:month>", views.monthly_challenges_by_num),

    path("<str:month>", views.monthly_challenges)  # Here month is the placeholder and the syntax to create is <>
    # Here datatype of month is passed as string

]
