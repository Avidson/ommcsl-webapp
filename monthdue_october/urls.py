from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from monthdue_october import views
from django.views.generic import TemplateView





app_name = 'monthdue_october'

urlpatterns = [
    path('', views.octoberDue, name='octoberdue'),
    path('payment-process', views.payment_process, name='payment-process'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-canceled/', views.payment_canceled, name='payment-cancelled'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)