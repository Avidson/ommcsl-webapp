from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from payment.views import *




app_name = 'payment'

urlpatterns = [
    path('payment-gateway', payment, name='payment-gateway'),
    path('process', payment_process, name='process'),
    path('payment-sucess', payment_success, name='payment-success'),
    path('payment-canceled', payment_canceled, name='payment-canceled'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)