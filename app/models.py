from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(("phone"))
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('famle', 'Famle')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    