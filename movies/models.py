from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Theatres(models.Model):
    name = models.CharField(max_length=100)
    # Foreign key
    movies = models.ManyToManyField(Movies)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Theatre"
        verbose_name_plural = "Theatres"