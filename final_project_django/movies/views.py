from django.shortcuts import render
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    pass

def research(request):
    pass

def recommend(request):
    pass

def detail(request, movie_pk):
    pass

def create_review(request, movie_pk):
    pass

def delete_review(request, movie_pk, review_pk):
    pass