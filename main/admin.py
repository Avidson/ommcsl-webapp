from django.contrib import admin
from main.models import *
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe



def payment_pdf(obj):
    url = reverse('main:youmade-payment_pdf', args=[obj.pk])
    return mark_safe(f'<a href="{url}">Generate PDF</a>') #This tells django template to allow this page to render
payment_pdf.short_description = 'Receipt'


class ProfileAdmin(admin.ModelAdmin):

    def export_to_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        content_disposition = f'attachment; filename={opts.verbose_name}.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = content_disposition
        writer = csv.writer(response)
        fields = [field for field in opts.get_fields() if not \
        field.many_to_many and not field.one_to_many]

        writer.writerow([field.verbose_name for field in fields])
        # Write data rows
        for obj in queryset:
            data_row = []
            for field in fields:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                data_row.append(value)
            writer.writerow(data_row)
        return response
    export_to_csv.short_description = 'Export to CSV'
    
    list_display = ('profile_owner', 'first_name', 'last_name', 'occupation', 'state_residence', 
    'home_address', 'phone_number', 'registration_fee', 'paid', 'email', 'payment_date','payment_ref',
    'passport', 'client_identification_number',
    payment_pdf
    )
    actions = [export_to_csv]


admin.site.register(Profile, ProfileAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
admin.site.register(Message, MessageAdmin)

#In line profile model


