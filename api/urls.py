# myapp/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import RegisterUser, LoginUser
from .views import (
    InAppDonationsDetail, InAppDonationsListView, 
    loan_request_listListView, ID_verification_ListView,
    Create_BranchListView, Create_BranchDetailView, UserRegistrationView
)


app_name = 'api'

urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('inapp-donation/', InAppDonationsListView.as_view(), name="inapp-donation"),
    path('inapp-donation/<pk>/', InAppDonationsDetail.as_view(), name='inapp-donation'),
    path('loan-request/', loan_request_listListView.as_view(), name='loan-request'),
    path('id-verification/', ID_verification_ListView.as_view(), name='id-verification'),
    path('branches/', Create_BranchListView.as_view(), name='branches'),
    path('branches/<pk>/', Create_BranchDetailView.as_view(), name='branch_details'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

