from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

percentage_calc = 100


class Payment_for_Share(models.Model):
    client_name = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default='0', editable=False)
    email = models.EmailField(default='example@email.com')
    timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    payment_ref = models.CharField(max_length=15, blank=True)
 
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.client_name.username

    def get_amount(self):
        return self.amount

class ShareHolding(models.Model):
    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    amount_bought = models.ForeignKey(Payment_for_Share, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    Share_return_at = models.FloatField(default=5, editable=False, help_text="Shares is at 5%")
    share_id = models.CharField(max_length=200, editable=False, default='0')
    there_was_a_withdrawal = models.BooleanField(default=False)


    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.client_name.username

    def get_amount_of_shares(self):
        return self.amount_bought

    def get_date(self):
        return self.date_bought

    def investment_return(self):
        return self.Share_return_at / percentage_calc * self.amount_bought.amount

class Withdrawal_Request(models.Model):
    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    share_id = models.CharField(max_length=200, editable=False, default='0')
    account_name = models.CharField(max_length=200, default='0')
    account_number = models.CharField(max_length=200, default='0')
    bank_name = models.CharField(max_length=200, default='0')
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default='0')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name.username






