from django.contrib import admin
from django.conf import settings
from Loan_Request.models import *
from django.db import models 
from Membership.models import Membership_verification

# Register your models here.


class loan_request_listAdmin(admin.ModelAdmin):

    list_display = ['client_name', 'loan_amount', 'loan_period', 'interest_rate', 
    'timestamp', 'loan_approval', 'emi', 'monthly_return', 
    'account_name', 'account_number', 'bank_name', 'loan_ref', 'loan_settled']


admin.site.register(loan_request_list, loan_request_listAdmin)
