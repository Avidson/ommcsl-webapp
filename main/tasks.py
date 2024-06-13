from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from main.models import *
from django.contrib.auth.models import User, auth
import requests
from django.core.mail import send_mail

@shared_task
def payment_completed(request, order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    your_invoice = 'your invoice'
    payment = Profile.objects.get(pk=order_id)
    user = request.user
    # create invoice e-mail
    subject = f'OMMCSL - Welcomes You On Board. {payment.pk}'
    message = f'''We are pleased to inform you {user} that you registration into
    the OMMCSL organization is official. Thank you for choosing to be part of this family, and
    we wish you a wonderful time here.'''
     
    email = EmailMessage(subject,
                         message,
                         'info@ommcsl.loan',
                         [payment.email])
    # generate PDF
    html = render_to_string('main/pdf.html', {'payment': payment})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'assets/css/passcode.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'{your_invoice}-{payment.payment_date}-{payment.pk}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()



