from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import statistics

class Movie(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def number_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def average_rating(self):

        sum = 0
        ratings = Rating.objects.filter(movie=self)

        for r in ratings:
            sum += r.stars
        
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):
    objects = models.Manager()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
