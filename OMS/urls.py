"""OMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from main.views import index_page, read_key_file
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('', index_page, name='home'),
    path('offline/', TemplateView.as_view(template_name='offline.html'), name='offline'),
    path('page-not-found/', TemplateView.as_view(template_name='page_not_found.html'), name='page-not-found' ),
    path('verification-required/', TemplateView.as_view(template_name='verification/needs_to_be_verified.html'), name='verification-required'),
    path('insufficient-fund/', TemplateView.as_view(template_name='insufficient.html'), name='insufficient-fund'),
    path('loanrequestSuccess/', TemplateView.as_view(template_name='loanrequestSuccess.html'), name='loanrequestSuccess'),
    path('pincreated/', TemplateView.as_view(template_name='pincreated.html'), name='pincreated'),
    path('data-submitted/', TemplateView.as_view(template_name='data_submitted.html'), name='data_submitted'),
    path('payment/', include('payment.urls', namespace='payment')),
    path('main/', include('main.urls', namespace='main')),
    path('Membership/', include('Membership.urls', namespace='Membership')),
    path('Shares/', include('Share.urls', namespace='Share')),
    path('inAppDonations/', include('inAppDonations.urls', namespace='inAppDonations')),
    path('Loan_Request/', include('Loan_Request.urls', namespace='Loan_Request')),
    path('Monthly_due/', include('Monthly_due.urls', namespace='Monthly_due')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls', namespace='api')),
    path('ads/', include('ads.urls', namespace='ads')),
    path('ecommerce/', include('ecommerce.urls', namespace='ecommerce')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('wallet/', include('wallet.urls', namespace='wallet')),
    path('waitlist/', include('waitlist.urls', namespace='waitlist')),
    path('monthdue_september/', include('monthdue_september.urls', namespace='monthdue_september')),
    path('monthdue_october/', include('monthdue_october.urls', namespace='monthdue_october')),
    path('monthdue_november/', include('monthdue_november.urls', namespace='monthdue_november')),
    path('monthdue_may/', include('monthdue_may.urls', namespace='monthdue_may')),
    path('monthdue_march/', include('monthdue_march.urls', namespace='monthdue_march')),
    path('monthdue_june/', include('monthdue_june.urls', namespace='monthdue_june')),
    path('monthdue_july/', include('monthdue_july.urls', namespace='monthdue_july')),
    path('monthdue_february/', include('monthdue_february.urls', namespace='monthdue_february')),
    path('monthdue_december/', include('monthdue_december.urls', namespace='monthdue_december')),
    path('monthdue_august/', include('monthdue_august.urls', namespace='monthdue_august')),
    path('monthdue_april/', include('monthdue_april.urls', namespace='monthdue_april')),
    path('.well-known/pki-validation/212DD3325F5E77649F6D2C0251BED93E.txt', read_key_file),
    path('ommcsl-logs/', admin.site.urls),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

