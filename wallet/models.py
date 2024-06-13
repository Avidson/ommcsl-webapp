from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.

class TopUp(models.Model):
    client_name = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default='0', editable=False)
    email = models.EmailField(default='example@email.com')
    timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    payment_ref = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Topup {self.id}'

    def get_amount(self):
        return self.amount




    
