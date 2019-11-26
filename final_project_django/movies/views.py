from django.shortcuts import render, get_object_or_404
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
    pass

@api_view(['GET'])
def admin_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

def research(request):
    pass

def recommend(request):
    pass

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie_id=movie_pk)
    return Response(serializer.data)

@api_view(['GET'])
def delete_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)