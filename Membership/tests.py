from django.test import TestCase
from .models import Membership_verification 
from django.conf import settings 
from django.contrib.auth.models import User 
from main.models import Profile
from django.db import models


# Create your tests here.

class Membership_verificationModelTest(TestCase):

    def test_create_verify_object(self):
        user = User(username='Johnbosco')
        obj = Membership_verification.objects.create(client_name=user, id_image='newphoto.png', verification_status=True)
        self.assertEqual(obj)
        self.assertEqual()

    


