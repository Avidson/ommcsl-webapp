from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from Share.models import *
from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404
import requests

@shared_task
def payment_completed(request):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
   
    payment = get_object_or_404(Payment_for_Share, client_name=request.user)
    user = request.user
   
    subject = f'OMMCSL - You Bought Our Shares'
    message = f'''Dear {user}, thank you for making payment for the purchase of our shares.
     Your payment of {payment.amount} has been registered successfully.'''
     
    email = EmailMessage(subject,
                         message,
                         'info@ommcsl.loan',
                         [payment.email])
    email.send()