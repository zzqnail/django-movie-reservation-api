from django.db.models import Model
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
