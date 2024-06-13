from django.contrib import admin
from ads.models import Display_ads
# Register your models here.


class Display_adsAdmin(admin.ModelAdmin):

    list_display = ['ads_title', 'approved', 'organisation_name', 'ads_url',
     'image', 'ads_starts', 'ads_end']
    
admin.site.register(Display_ads, Display_adsAdmin)
