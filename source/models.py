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
    reco = models.BooleanField(null=True)
    essay = models.BooleanField(null=True)
    info = models.BooleanField(null=True)
    financial = models.BooleanField(null=True)
    transcripts = models.BooleanField(null=True)
    test = models.BooleanField(null=True)
    extra = models.BooleanField(null=True)
    def __str__(self):
        return f"{self.user} : {self.university_name}"

class UniversityName(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    univ_name = models.CharField(max_length=40, null=True)
    prompt = models.TextField()
    content= models.TextField()

    def __str__(self):
        return f"{self.user} : {self.prompt}"


class Councellor(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user}"
