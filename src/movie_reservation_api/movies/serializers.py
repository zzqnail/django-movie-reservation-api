
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'duration_min',
            'director',
            'description',
            'premiere',
            'age_rating'
        ]