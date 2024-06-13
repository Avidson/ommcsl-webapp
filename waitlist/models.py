from django.db import models

# Create your models here.

class waitlist(models.Model):
    name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    phone_number = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
