from django.db import models
from django.contrib.auth.models import User



class Resume(models.Model):
    name = models.CharField(max_length=100)
    role =  models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.IntegerField()
    skills = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    salary = models.IntegerField()
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    position = models.CharField(max_length=100)
    gap=  models.CharField(max_length=100)
    age =  models.IntegerField()
    qualification =  models.CharField(max_length=100)
    my_file = models.FileField(upload_to="images", blank=True)

    def __str__(self):
        return str(self.id)
    
