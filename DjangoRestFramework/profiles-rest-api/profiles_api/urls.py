from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# This is how we register a viewset which we created in the views.py
router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view', views.HelloAPIView.as_view()),
    path("", include(router.urls))  # As we have registered the viewsets with the router, it creates a list of URLs and
    # we need to include them in the path.
]
