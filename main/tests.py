'''from django.test import TestCase
import pytest
# Create your tests here.
from main.models import Profile 


def Profile(TestCase):
    add_profile = Profile.objects.get_or_create(profile_owner='Johnny', occupation='Student', email='csunny@gmail.com')
    return add_profile

def test_Profile():
    pro = Profile()
    assert pro == Profile.objects.get_or_create(profile_owner='Chidi', occupation='Engineer', email='chief@gmail.com')
'''

