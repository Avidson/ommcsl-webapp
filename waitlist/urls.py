from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView



app_name = 'waitlist'

urlpatterns = [
    path('waitlisting/', views.waitlist_view, name='waitlisting'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)