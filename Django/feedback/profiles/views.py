from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
# Create your views here.


def store_file(file):
    with open("temp/image.heic", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", context={
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # store_file(request.FILES["image"])
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html", context={
            "form": submitted_form
        })