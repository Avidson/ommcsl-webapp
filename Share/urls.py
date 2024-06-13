from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Shares'

urlpatterns = [
    path('share_dex/', views.share_holding, name='share_dex'),
    path('withdrawal_request/', views.withdrawal_request, name='withdrawal_request'),
    path('share_payment_view/', views.send_payment_for_share, name='share_payment_view'),
    path('process/', views.payment_process, name='process'),
    path('payment-sucess/', views.payment_success, name='payment-success'),
    path('payment-canceled/', views.payment_canceled, name='payment-canceled'),
    path('shares_detail/', views.shares_detail_view, name='shares_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)