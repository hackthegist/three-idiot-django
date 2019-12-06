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
    directorNm = models.CharField(max_length=45)
    genres_id = models.ManyToManyField(Genre, related_name="movies")
    # genresNm = models.CharField(max_length=150)
    prdtYear = models.IntegerField()
    openDt = models.IntegerField()
    showTm = models.IntegerField()
    nationNm = models.CharField(max_length=45)
    actorsNm = models.CharField(max_length=150)
    watchGradeNm = models.CharField(max_length=100)
    companyNmDict = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    userRating = models.CharField(max_length=45)
    audiAcc = models.CharField(max_length=45)
    thumbsNm = models.CharField(max_length=500)
    thumbsImage = models.TextField()

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