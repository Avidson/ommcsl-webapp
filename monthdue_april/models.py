from django.db import models
from django.conf import settings


# Create your models here.

class AprilDue(models.Model):

    client_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default='0', editable=False)
    email = models.EmailField(default='example@email.com')
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_ref = models.CharField(max_length=25, blank=True)
    remark = models.CharField(max_length=200, default='Your payment is upto date!')

    def __str__(self):
        return self.client_name.username

    def get_amount(self):
        return self.amount
