from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

from Pathway_to_Marvels_Greatest import settings


# Create your models here.
class Users(AbstractUser):
    user_email = models.EmailField(max_length=255)
    user_password = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.IntegerField()


class Characters(models.Model):
    name = models.CharField(max_length=255)


class Comics(models.Model):
    title = models.CharField(max_length=255)
    publicationDate = models.DateField()
    summary = models.TextField()
    linkForPurchase = models.CharField(max_length=500)
    characters = models.ManyToManyField(Characters, through="ComicCharacters")

class ComicCharacters(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comics, on_delete=models.CASCADE)


class Reviews(models.Model):
    title = models.CharField(max_length=255)
    reviewDate = models.DateField()
    body = models.TextField()
    rating = models.IntegerField(default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comics, on_delete=models.CASCADE)

class ForumComments(models.Model):
    time_date = models.DateTimeField()
    comment = models.TextField()
    comm_time_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Bookmarks(models.Model):
    link = models.CharField(max_length=500)
    creationDate = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Friendship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_friends_with')

    class Meta:
        unique_together = ['user', 'friend']
