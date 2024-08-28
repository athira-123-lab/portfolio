from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.CharField(max_length=200)
    bio=models.CharField(max_length=200)
    pic=models.ImageField(upload_to='picture_pics/',blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.user)