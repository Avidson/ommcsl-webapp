#urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from main import views



app_name = 'main'

urlpatterns = [
    
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('services/', views.services_page, name='services'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('e-transact/', views.create_transanction, name='e-transact'),
    path('user-profile-update/', views.ProfileEdit, name='user-profile-update'),
    path('registration-fee/', views.registration_fee_payment, name='registration-fee'),
    path('processing-payment/', views.payment_process, name='processing-payment'),
    path('payment-sucess/', views.payment_success, name='payment-success'),
    path('payment-canceled/', views.payment_canceled, name='payment-canceled'),
    path('youmade-payment_pdf/<pk>/pdf/', views.payment_pdf_generator, name='youmade-payment_pdf'),
    path('account_statement/', views.generate_account_statement, name='account_statement'),
    path('account_statement_pdf', views.account_statement_generate_pdf, name='account_statement_pdf'),
    path('view-profile/<pk>/', views.user_profile, name='view-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)