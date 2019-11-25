from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research, name='research'),
    path('recommend/', views.recommend, name='recommed'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/reviews/create/', views.create_review, name='create_review'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
]