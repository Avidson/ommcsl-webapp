
from celery import shared_task
from django.core.mail import send_mail
from ecommerce.models import OrderItem

@shared_task
def payment_created(payment_id):
    """
    Task to send an e-mail notification when an payment is
    successfully created.
    """
    payment = OrderItem.objects.get(id=payment_id)
    subject = f'Paymment with ref: {payment.id}'
    message = f'Dear {payment.client_name},\n\n' \
              f'You have successfully made a donation payment to OMMCSL Multipurpose Cooperative.' \
              f'Your payment ID is {payment.id}. \n\n' \
              f'Amount paid was the sum of {payment.amount}'\
              f'Thank you for believing in us.'
                

    mail_sent = send_mail(subject,
                          message,
                          'info@ommcl.loan',
                          [payment.email])
    return mail_sent