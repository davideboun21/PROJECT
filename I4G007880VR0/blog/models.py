from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), null=True)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
