from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.CharField(max_length=200)
    bio=models.CharField(max_length=200)
    image = models.ImageField(upload_to='image_url/')


    def __str__(self):
        return '{}'.format(self.user)

