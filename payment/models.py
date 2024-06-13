from django.db import models
from django.shortcuts import reverse

# Create your models here.

PAYMENT_OPTIONS = [
    ('Support Donation', 'Support Donation'),
    ('Membership Registration', 'Membership Registration'),
]


class Payment(models.Model):
    first_name = models.CharField(max_length=100, editable=False)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    amount = models.FloatField(default='0', editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment_purpose = models.CharField(max_length=200)
    paystack_ref = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Payment {self.id}'

    def get_amount(self):
        return self.amount
