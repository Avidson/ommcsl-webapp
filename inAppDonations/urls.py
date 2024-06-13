from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from inAppDonations.views import *




app_name = 'inAppDonations'

urlpatterns = [
    path('payment-gateway/', payment, name='payment-gateway'),
    #path('payment-gateway/<pk>/', payment, name='payment-gateway'),
    path('processing-payment/', payment_process, name='processing-payment'),
    path('payment-sucess/', payment_success, name='payment-success'),
    path('payment-canceled/', payment_canceled, name='payment-canceled'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
