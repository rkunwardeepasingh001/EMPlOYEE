from django.db import models

# Create your models here.
class Emp(models.Model):
  name = models.CharField(max_length=30,null=True,blank=True)
  title = models.CharField(max_length=30,null=True,blank=True)
  location = models.CharField(max_length=30,null=True,blank=True)
  age = models.IntegerField(null=True,blank=True)
  salary = models.IntegerField(null=True,blank=True)
  