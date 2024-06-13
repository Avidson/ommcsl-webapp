from django.contrib import admin
from .models import *
# Register your models here.



class ShareHoldingAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'amount_bought', 'timestamp', 'there_was_a_withdrawal']
admin.site.register(ShareHolding, ShareHoldingAdmin)

class Payment_for_ShareAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'amount', 'email', 'paid', 'timestamp', 'payment_ref']
admin.site.register(Payment_for_Share, Payment_for_ShareAdmin)

class Withdrawal_RequestAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'share_id', 'account_name', 'account_number', 'amount', 'bank_name', 'timestamp']
admin.site.register(Withdrawal_Request, Withdrawal_RequestAdmin)