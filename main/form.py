from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

""" class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password1'] """

class EtransactForm(forms.Form):
    transactionPin = forms.IntegerField()
    