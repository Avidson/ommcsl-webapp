from django.contrib import admin

# Register your models here.
from . models import Create_Branch



class Create_BranchAdmin(admin.ModelAdmin):

    list_display = [
        'branch_name', 'address', 'date', 'creator', 'phone_contact'  
    ]

admin.site.register(Create_Branch, Create_BranchAdmin)



