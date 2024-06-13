from django.db import models
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from Membership.models import Membership_verification
from custom_code.utils import calculate_emi
import sys
# Create your models here.


class loan_request_list(models.Model):
    client_name =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    loan_amount = models.FloatField(default='0', editable=False)
    loan_period = models.DecimalField(decimal_places=2, max_digits=20, default='0', editable=False)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=20, default=10, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    loan_approval = models.BooleanField(default=False)
    account_name = models.CharField(max_length=200, default='None')
    account_number = models.CharField(max_length=200, default='None')
    bank_name = models.CharField(max_length=200, default='None')
    purpose_for_loan = models.TextField(default='None')
    loan_ref = models.CharField(max_length=500, default='None')
    emi = models.FloatField(default='0', editable=False)
    monthly_return = models.FloatField(default='0', editable=False)
    loan_settled = models.BooleanField(default=False)

    class Meta:
        ordering = (('-timestamp'),)
        index_together = (('id'),)

    def __str__(self):
        return self.client_name.username

    def get_loan_amount(self):
        return self.loan_amount

    def save(self, *args, **kwargs):
        # Calculate and set the EMI before saving the Loan object
        percent = 100
        try:
            monthly_roi = self.loan_amount * self.interest_rate / percent  # Monthly interest rate
            n = monthly_roi * self.loan_period  # Number of periods (months)
            self.emi = self.loan_amount + n
            self.monthly_return = monthly_roi
        except SystemExit as e:
            sys.exit('There was an error {}'.format(e))

        try:
            """ An extract with datetime to append as ref
            code for all loan request entries """
            from datetime import datetime

            now = datetime.now()
            date_extract = f'{now:%H%M%S}'
            extract = self.account_number[3:-1]
            main_date_extract = 2023 + 1
            self.loan_ref = str(extract) + str(main_date_extract) + date_extract

        except SystemExit as e:
            sys.exit('There was an error {}'.format(e))

        super(loan_request_list, self).save(*args, **kwargs)

    def get_emi_for_loan(self):
        return self.emi




