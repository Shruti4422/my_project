from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.user.username
