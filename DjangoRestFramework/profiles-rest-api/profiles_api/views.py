from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as a function (get, post, put, patch and delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs'",
        ]

        return Response(
                        {'message': "Hello",
                         "an_apiview": an_apiview
                         }
                        )

    def post(self, request):
        """Create a Hello Message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello! {name}"
            return Response({
                "message": message
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object. A put method updates the entire object"""
        return Response({
            "method": "PUT"
        })

    def patch(self, request, pk=None):
        """Handle a partial update of an object. It only updates the fields provided in the reqeust"""
        return Response({
            "method": "PATCH"
        })

    def delete(self, request, pk=None):
        """Handles deleting an object."""

        return Response({
            "method": "DELETE"
        })


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to the URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({
            "message": "Hello",
            'a_viewset': a_viewset
        })

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello! {name}"
            return Response({
                "message": message
            })
        else:
            return Response(serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)

    def retrieve(self, request, pk=None):
        """Handle getting objects using its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object using its ID"""
        return Response({
            "http_method": "PUT"
        })

    def partial_update(self, request, pk=None):
        """Handle updating part of an object using its ID"""
        return Response({
            "http_method": "PATCH"
        })
