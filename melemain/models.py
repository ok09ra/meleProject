from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AudioModel(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    audio = models.FileField(upload_to="")
    iine = models.IntegerField(null = True, blank = True, default = 0)
    iine_people = models.TextField()
    