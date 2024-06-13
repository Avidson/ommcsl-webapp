from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView



app_name = 'Membership'

urlpatterns = [
    path('register/', views.member_registration, name='register'),
    path('success/', views.successful, name='success'),
    path('create_account/', views.create_account, name='create_account'),
    path('lets-verify-you/', views.verification_view, name='lets-verify-you'),
    path('verified/', TemplateView.as_view(template_name='verification/verified.html'), name='verified'),
    path('pending/', TemplateView.as_view(template_name='verification/pending.html'), name='pending'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)