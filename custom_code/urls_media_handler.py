from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
import os 
import sys




#def media_functool():
#    try:

#        urlpatterns = ['*']

#        if settings.DEBUG == True:
#            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#        if settings.DEBUG == False:
#            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#    except SystemExit as e:
#        sys.exit('There was an error {}'.format(e))

#if "__main__" == __name__ :
#    media_functool()
