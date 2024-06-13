from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from Monthly_due import views
from django.views.generic import TemplateView






app_name = 'Monthly_due'

urlpatterns = [
    path('', views.month_indexview, name='home_monthly'),
    path('januarydue/', views.januaryDue, name='januarydue'),
    path('payment-process', views.payment_process, name='payment-process'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-canceled/', views.payment_canceled, name='payment-cancelled'),
    path('payment-upto-date/', TemplateView.as_view(template_name='verification/needs_to_be_verified.html'), name='payment-upto-date'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)