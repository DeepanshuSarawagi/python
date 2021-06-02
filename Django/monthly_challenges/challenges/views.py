from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string  # We import this module to render the HTML document as string
# and then return the response back to client

monthly_challenges = {
    "january": "Walk for 30 minutes a day",
    "february": "Learn Django for 20 minutes a day",
    "march": "Do yoga to correct your spine posture",
    "april": "Walk for 30 minutes a day",
    "may": "Learn Django for 20 minutes a day",
    "june": "Do yoga to correct your spine posture",
    "july": "Walk for 30 minutes a day",
    "august": "Learn Django for 20 minutes a day",
    "september": "Do yoga to correct your spine posture",
    "october": "Walk for 30 minutes a day",
    "november": "Learn Django for 20 minutes a day",
    "december": "Do yoga to correct your spine posture",
}

# Create your views here.

# Remember that every view is a standalone function/class


# def index(request):
#     return HttpResponse("This Works!")  # Created a function which will return the response to a request
#
#
# def feb_index(request):
#     return HttpResponse("This is a response for February index")  # Created a fn/view which will return the response
# # for a request if URI is /challenges/february/
#
#
# def march(request):
#     return HttpResponse("learn a new skill/programming language for 20 minutes every day")

# Commenting the above code briefly so that we can create dynamic views

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_url = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_url}\">{capitalized_month}</a></li>"
    response_data = f"""
        <h1>Hello! Welcome to your monthly challenges page</h1>
        <p1>Click on the below links to view your challenges</p1>
        <ul>{list_items}</ul>
    """
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = "<h1>{}</h1>".format(challenge_text)
        return render(request=request, template_name="challenges/challenge.html", context={"text": challenge_text
            , "month": month.capitalize()})
        # Commenting below code because we will be rendering html using render module
        # response_data = render_to_string("challenges/challenge.html")  # path to html doc to render to string
        # return HttpResponse(response_data)
        # We pass the third positional keyword argument called context which will be used to inject dynamic content in
        # the HTML page using DTL
    except:
        return HttpResponseNotFound("<h1>This month does not exist!</h1>")


def monthly_challenge_by_num(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]  # We are getting the month as an integer argument and getting the actual month
        # from the dictionary using the key. This key is got from the list months by accessing month argument as index
        redirect_path = reverse("month-challenge", args=[redirect_month])
        # Reverse function allows us to construct paths by referring to the name values of URLS
        # in app specific urls.py. It will then prefix the path with URI in the project specific urls.py which is
        # /challenges/
        # It also accepts one more args as array which we want to append after /challenges/ and that is passed as array
        # hence the final result would be challenges/ + redirect_month e.g., /challenges/january
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("<h1>This month does not exist!</h1>")
