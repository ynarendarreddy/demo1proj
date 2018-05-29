from django.db import models
class book(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bookname=models.CharField(max_length=20)
class author(models.Model):
     authorid=models.IntegerField(primary_key=True)
    authorname=models.CharField(max_length=20)



# Create your models here.
