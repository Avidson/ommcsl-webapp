from django.apps import AppConfig


class MonthlyDueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Monthly_due' 

class MyAdminConfig(AppConfig):
    default_site = "Monthly_due.admin"


