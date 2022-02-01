
from django.db import models

# Create your models here.

class Skills(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    level=models.CharField(max_length=100, null=True, blank=True)

class Education(models.Model):
    institutionname=models.CharField(max_length=100, null=True, blank=True)
    degree=models.CharField(max_length=100, null=True, blank=True)
    date=models.CharField(max_length=100, null=True, blank=True)

class Experience(models.Model):
    org=models.CharField(max_length=100, null=True, blank=True)
    role=models.CharField(max_length=100, null=True, blank=True)
    time=models.CharField(max_length=100, null=True, blank=True)



class Project(models.Model):
    Project_Name=models.CharField(max_length=100, null=True, blank=True)
    category=models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=3000, null=True, blank=True)
    url=models.URLField()

class Publication(models.Model):
    paper_name=models.CharField(max_length=1000, null=True, blank=True)
    place=models.CharField(max_length=1000, null=True, blank=True)
    date=models.CharField(max_length=1000, null=True, blank=True)
    paper_url=models.CharField(max_length=1000, null=True, blank=True)

