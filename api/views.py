from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from rest_framework.authtoken.models import Token
from main.models import Profile
from inAppDonations.models import InAppDonations 
from Loan_Request.models import loan_request_list 
from Membership.models import Membership_verification
from Share.models import *
from Monthly_due import *
from branches.models import Create_Branch
from feedback.models import Feedbacks
from rest_framework import generics
from .serializers import (
    InAppDonationsSerializer, loan_request_listSerializer,
    Membership_verificationSerializer, Create_BranchSerializer, 
    FeedbacksSerializer, UserRegistrationSerializer
)
from django.contrib.auth.models import User, auth
from django.urls import reverse

#Account Registration View
class RegisterUser(APIView):
    def post(self, request):
        if request.method == 'POST':
            data = request.data

            username = data.get('username')
            password = data.get('password')
            re_password = data.get('retypepassword')

            if not username or not password:
                return Response({'Error' : 'User detail invalid' })
            
            newUser = User.objects.create_user(username=username, password=password)

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


#Our Api Login View
class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'username': user.username}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class InAppDonationsListView(generics.ListAPIView, APIView):
    queryset = InAppDonations.objects.all()
    serializer_class = InAppDonationsSerializer

class InAppDonationsDetail(generics.RetrieveAPIView, APIView):
    queryset = Profile.objects.all()
    serializer_class = InAppDonationsSerializer

class loan_request_listListView(generics.ListAPIView, APIView):
    authentication_classes = [BasicAuthentication]

    queryset = loan_request_list.objects.all()
    serializer_class = loan_request_listSerializer

    def post(self, request):
        if request.method == 'POST':
            data = request.data

            client_name = data.get('client_name')
            loan_amount = data.get('loan_amount')
            loan_period = data.get('loan_period')
            account_name = data.get('account_name')
            account_number = data.get('account_number')
            bank_name = data.get('bank_name')
            purpose_for_loan = data.get('purpose_for_loan')
            
            loanObject = loan_request_list.objects.create_user(
                client_name=client_name, loan_amount=loan_amount,
                loan_period=loan_period, account_name=account_name,
                account_number=account_number, bank_name=bank_name,
                purpose_for_loan = purpose_for_loan 
                )
            return Response({'message': 'Your application has been submitted'}, status=status.HTTP_201_CREATED)


""" API code for id verification """
class ID_verification_ListView(generics.ListAPIView, APIView):
    queryset = Membership_verification.objects.all()
    serializer_class = Membership_verificationSerializer

    def post(self, request):
        if request.method == 'POST':
            data = request.data

            phone_number = data.get('phone_number')
            id_type = data.get('id_type')
            id_image = data.get('id_image')
            
            id_object = Membership_verification.objects.create(
                phone_number = phone_number,
                id_type = id_type,
                id_image = id_image,
                )
            return Response({'message': 'Identity has been sent for verification'}, status=status.HTTP_201_CREATED)

class Create_BranchListView(generics.ListAPIView, APIView):
    permission_classes=[AllowAny]

    queryset = Create_Branch.objects.all()
    serializer_class = Create_BranchSerializer

class Create_BranchDetailView(generics.RetrieveAPIView):
    permission_classes=[AllowAny]

    queryset = Create_Branch.objects.all()
    serializer_class = Create_BranchSerializer

class AddingNewBranch(APIView):
    def post(self, request):
        serializer = Create_BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbacksListView(generics.ListAPIView, APIView):
    permission_classes=[AllowAny]
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer
    
class SendingFeedback(APIView):
    def post(self, request):
        serializer = FeedbacksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)