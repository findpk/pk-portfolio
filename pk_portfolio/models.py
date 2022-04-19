from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=25,blank=False)
    role = models.CharField(max_length=25,blank=False)
    current_organization = models.CharField(max_length=25,blank=False)
