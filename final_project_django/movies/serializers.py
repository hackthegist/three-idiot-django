from rest_framework import serializers
from .models import Genre, Movie, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'summary', 'genresNm', 'prdtYear', 'openDt', 'showTm', 'nationNm', 'actorsNm', 'watchGradeNm', 'companyNmDict', 'link', 'image', 'userRating', 'audiAcc',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'comment', 'score', 'user', 'movie_id',)

class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ('review_set',)