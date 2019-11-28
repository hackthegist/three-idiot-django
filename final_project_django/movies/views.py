from django.shortcuts import render, get_object_or_404
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Review
import random

# Create your views here.

def home(request):
    pass

@api_view(['GET'])
def admin_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def research(request):
    movies = Movie.objects.all()
    research_movies = []
    while len(research_movies) < 15:
        num = random.randrange(1, 1001)
        if num not in research_movies:
            research_movies.append(num)
    queryset = Movie.objects.filter(pk__in=research_movies)
    serializer = MovieSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def recommend(request):
    movies = Movie.objects.all()
    movie_scores = []
    movie_ids = []
    recommended_movies = []
    for movie_data in request.data:
        for movie in movies:
            temp_score = 0
            if movie.director == movie_data.director:
                temp_score += 1
            if movie.genre == movie_data.genre:
                temp_score += 1
            if movie_data.showTm-30 <= movie.showTm <= movie_data.showTm+30:
                temp_score += 1
            if movie.nationNm == "한국":
                if movie_data.nationNm == "한국":
                    temp_score += 1
            else:
                if movie_data.nationNm != "한국":
                    temp_score += 1
            if movie.watchGradeNm == movie_data.watchGradeNm:
                temp_score += 1
            for actor in movie.actors:
                if actor in movie_data.actors:
                    temp_score += 1
                    break
            movie_scores.append(temp_score)
    pivot_score = (max(movie_scores) + min(movie_scores)) // 2
    for idx in range(1, 1001):
        if pivot_score < movie_scores[idx]:
            movie_ids.append(idx+1)
    checked = [False for i in range(1000)]
    while len(recommended_movies) < 5:
        num = random.randrange(1, 1001)
        if num in movie_ids:
            if cheched[num-1] == False:
                checked[num-1] = True
                recommended_movies.append(num)
    queryset = Movie.objects.filter(pk__in=recommended_movies)
    serializer = MovieSerializer(queryset, many=True)
    return Response(serializer.data)

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