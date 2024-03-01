from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    user_password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.IntegerField()


class CachedCharacters(models.Model):
    name = models.CharField(max_length=255)


class CachedComics(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    character_id = models.IntegerField()
    character_id2 = models.ForeignKey(CachedCharacters, on_delete=models.CASCADE)


class ForumComments(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    time_date = models.DateTimeField()
    comment = models.TextField()
    comm_time_date = models.DateTimeField()
    fKey = models.ForeignKey(Users, on_delete=models.CASCADE)
