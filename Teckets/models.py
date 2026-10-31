from django.db import models


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=30)
    def __str__(self):
        return self.movie



class Guest(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    def __str__(self):
        return self.name




class Reservation(models.Model):
    guest = models.ForeignKey(Guest , related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie , related_name='reservation', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.movie)


