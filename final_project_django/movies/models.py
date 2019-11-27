from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField()
    director = models.CharField(max_length=45)
    genre = models.ManyToManyField(Genre, related_name="movies", blank=True) # FK : 다른 모델의 pk를 가져온 것 : ex> 학생 1반 2반 등..
    prdtYear = models.IntegerField()
    showTm = models.IntergerField()
    nationNm = models.CharField(max_length=45)
    actors = models.CharField(max_length=150)
    watchGradeNm = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Review(models.Model):
    comment = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False)

    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return f'{self.score} {self.comment}'