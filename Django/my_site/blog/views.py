from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return None


def post_detail(request):
    return None