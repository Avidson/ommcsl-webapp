from django.db import models

# Create your models here.


class Create_Branch(models.Model):
    branch_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    creator = models.CharField(max_length=300)
    phone_contact = models.CharField(max_length=20, default='090988777877')
    date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.creator
