from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404, redirect
import requests

# Create your models here.

class InAppDonations(models.Model):
    client_name = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default='0')
    email = models.CharField(max_length=200, default='None')
    timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    payment_purpose = models.CharField(max_length=200)
    payment_ref = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'InAppDonations {self.id}'

    def get_amount(self):
        return self.amount
