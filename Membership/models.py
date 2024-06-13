from django.db import models
from main.models import Profile
from django.conf import settings
# Create your models here.



IDS = (
    ('National Identification Number(NIN)', 'National Identification Number(NIN)'),
    ('Voters Card', 'Voters Card'),
    ('Driver License', 'Driver License'),
    ('International Passport', 'International Passport'),
)

class Membership_verification(models.Model):
    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='0')
    id_type = models.CharField(max_length=200, default='None')
    id_image = models.ImageField(upload_to='idFolder/')
    timestamp = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=200, default='090')
    verification_status = models.BooleanField(default=False)

    class Meta:
        ordering = (('-timestamp'),)
        index_together = (('id'),)

    def __str__(self):
        return self.client_name.username

class Membership_Registration(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    next_of_kin = models.CharField(max_length=200)
    next_of_kin_phone = models.CharField(max_length=200)
    reg_date = models.CharField(max_length=200)
    identification = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    passport = models.ImageField()

    def __str__(self):
        return self.surname



