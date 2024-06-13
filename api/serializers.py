from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Profile
from inAppDonations.models import InAppDonations
from Loan_Request.models import loan_request_list 
from Membership.models import Membership_verification
from branches.models import Create_Branch
from ads.models import Display_ads
from feedback.models import Feedbacks
from ecommerce.models import Product
 
""" In app donations serializer """
class InAppDonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InAppDonations
        fields = ['client_name', 'amount',]


""" Loan Request serializer """
class loan_request_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan_request_list
        fields = ['loan_amount', 'loan_period']

""" Membership verification serializer """
class Membership_verificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership_verification
        fields = ['client_name', 'phone', 'verification_status']


class Create_BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create_Branch
        fields = ['branch_name', 'address', 'creator', 'phone_contact' ]


class Display_adsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Display_ads
        fields = ['ads_title', 'organisation_name', 'image', 'ads_url']

class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = ['name', 'message']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['name','price']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 

