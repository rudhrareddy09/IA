from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField()

    def __str__(self):
        return f"{self.name}"



class UniversityRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=40)
    programme = models.CharField(max_length=30)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.user} : {self.university_name}"
