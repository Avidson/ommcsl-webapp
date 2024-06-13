from django.contrib import admin
from . models import *
import csv
import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe
# Register your models here.


class Paymentdmin(admin.ModelAdmin):

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

    list_display = ('id','first_name', 'last_name', 'email', 'amount', 
                    'created', 'updated', 'paid', 'paystack_ref', 'payment_purpose'
                    )
    list_filter = [
            'paid', 'created', 'updated'
    ]
    actions = [export_to_csv]
admin.site.register(Payment, Paymentdmin)
