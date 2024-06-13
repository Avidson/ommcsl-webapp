from django.db import models
import sys 
from django.db import models
from django.contrib.auth.models import User
from custom_code.utils import calculate_emi
import math
from django.conf import settings
from wallet.models import TopUp
from django.db.models import Sum
from custom_code.pass_code import pass_argument
from datetime import datetime
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    profile_owner = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, editable=False, default=0)
    first_name = models.CharField(max_length=150, default='your first name', editable=False)
    last_name = models.CharField(max_length=150, default='your first name', editable=False)
    occupation = models.CharField(max_length=150, default='your occupation', editable=False)
    state_residence = models.CharField(max_length=200, default='Home address', editable=False)
    home_address = models.CharField(max_length=200, default='address', editable=False)
    phone_number = models.CharField(max_length=200, default='0908987679', editable=False)
    email = models.CharField(max_length=200, default='example@email.com')
    registration_fee = models.DecimalField(decimal_places=2, max_digits=20, default='0', editable=False)
    payment_date = models.DateField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment_ref = models.CharField(max_length=200, default='None', editable=False)
    passport = models.ImageField(default='None', upload_to='profilePassports/')
    account_balance = models.DecimalField(decimal_places=2, max_digits=20, default='0', editable=False)
    transactionPin = models.IntegerField(default=0)
    client_tag = models.CharField(max_length=200, default='OMMCSL')
    client_identification_number = models.CharField(max_length=200, default='')
    next_of_kin_full_name = models.CharField(max_length=200, default='')
    next_of_kin_phone_number = models.CharField(max_length=200, default='')
    next_of_kin_address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.home_address
    
    def get_registration_fee(self):
        return self.registration_fee
    
    def get_absolute_url(self):
        return reverse('main:view-profile', args=[self.pk])

    def save(self, *args, **kwargs):
        encrypt_pin = pass_argument(self.transactionPin)
        self.transactionPin = encrypt_pin
        super(Profile, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        """ An extract with datetime to append as clife serialcode """
        now = datetime.now()
        date_extract = f'{now:%H%M%S}'
        client_initial = self.client_tag
        self.client_identification_number = str(client_initial)  + date_extract
        super(Profile, self).save(*args, **kwargs)

class Dashboard(models.Model):
    pass 

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


    
    




        



    

 

