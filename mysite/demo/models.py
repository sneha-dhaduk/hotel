from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=10)
    roll_no=models.IntegerField()
    exam_date=models.DateField()
    email_id=models.EmailField()

    def __str__(self):
        return self.name
    
class cake(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=15)
    contain=HTMLField()
    price=models.CharField(max_length=2)

class car(models.Model):
    name=models.CharField(max_length=15)
    color=models.CharField(max_length=15)
    price=models.IntegerField()

    def __str__(self):
        return self.name