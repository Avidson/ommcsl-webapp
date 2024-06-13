from django.contrib import admin
from waitlist.models import waitlist
# Register your models here.

class waitlistAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
admin.site.register(waitlist, waitlistAdmin)