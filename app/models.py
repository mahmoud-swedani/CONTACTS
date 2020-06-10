from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    emile = models.EmailField(max_length=100)
    phone = models.ImageField()
    info = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male')
        ('famle', 'famle')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_add = models.DateField(auto_now_add=True)