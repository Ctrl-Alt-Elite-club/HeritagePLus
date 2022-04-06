
from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    fn = models.CharField(max_length=46)
    ln = models.CharField(max_length=46)
    email = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to='uploads/',default='logo.png')

class Monument(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    detail = models.TextField

class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    monument = models.ForeignKey(Monument,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class MonumentImage(models.Model):
    id = models.IntegerField(primary_key=True)
    monument = models.ForeignKey(Monument,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='monuments/',default='logo.png')

class ReportImage(models.Model):
    id = models.IntegerField(primary_key=True)
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='reports/',default='logo.png')