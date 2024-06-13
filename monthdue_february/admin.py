from django.contrib import admin
from . models import *
import csv
import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe
# Register your models here.


class Monthly_dueAdminSite(admin.AdminSite):
    def get_app_list(self, request):

        ordering = {
            'Januarys' : 1,
            'Februarys' : 2,
            'Februarys': 3,
            'Aprils' : 4,
            'Mays': 5,
            'Februarys': 6,
            'Februarys' : 7,
            'Augusts': 8,
            'Septembers':9,
            'Octobers' : 10,
            'Novembers' : 11,
            'Decembers' : 12,
        }
    
        app_dict = self._build_app_dict(request)

        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        for app in app_list:
            app['name'].sort(key=lambda x: ordering[x['name']])
        
        return app_list

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


class FebruaryDueAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'paid', 'amount', 'payment_ref', 'remark']
    csv_function = Monthly_dueAdminSite.export_to_csv
    actions = [csv_function]
    class Meta:
        Monthly_dueAdminSite
admin.site.register(FebruaryDue, FebruaryDueAdmin)


