from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    email_id = models.EmailField()
    deparment = models.CharField(max_length=50)
    deatOfJoining = models.DateField()
    status = models.CharField(max_length=30)
    projectDomain = models.CharField(max_length=30)