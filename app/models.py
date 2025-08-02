from django.db import models

# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=200)
    profession=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='images', blank=True, null=True)

class Project(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images',blank=True, null=True)
    description=models.TextField(blank=True, null=True)

class Service(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images',blank=True, null=True)
    description=models.TextField(blank=True, null=True)

class Skill(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images', blank=True, null=True)
    description=models.ImageField(upload_to='images', blank=True, null=True)

class Contact(models.Model):
    address=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.IntegerField()
   


