from django.shortcuts import render, get_object_or_404
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Review

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
    # review = Review(request.data)
    # review.score = 1
    # review.user = request.user
    # review.movie_id = movie_pk
    # review.save()
    # return Response({message: "리뷰가 생성되었습니다."})
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie_id=movie_pk)
    # return Response(serializer.data)
    return Response(status=200)

@api_view(['GET'])
def delete_review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    # return Response(serializer.data)
    return Response(status=200)