from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from Loan_Request.views import *
from django.views.generic import TemplateView




app_name = 'Loan_Request'

urlpatterns = [
    path('loan-request/', loan_request, name='loan-request'),
    path('approved-loans/', approved_loans, name='approved-loans'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)