from django.contrib import admin
from .models import Category, Product
from django.contrib import admin
from .models import Order, OrderItem, Review, Property_enquirie
import csv
import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'discount_available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):

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

    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'phone', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]
admin.site.register(Order, OrderAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Review, ReviewAdmin)

class Property_enquirieAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'phone', 'email', 'message']

admin.site.register(Property_enquirie, Property_enquirieAdmin)