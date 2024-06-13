from django.contrib import admin
from feedback.models import Feedbacks
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'message']

admin.site.register(Feedbacks, FeedbackAdmin)