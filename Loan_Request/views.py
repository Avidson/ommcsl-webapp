from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
# Create your views here.
from .models import *
from Membership.models import Membership_verification


@login_required
def loan_request(request, *args, **kwargs):

    form = loan_request_list(request.POST)

    try:
        if Membership_verification.objects.filter(client_name=request.user).exists():
            loan_obj = get_object_or_404(Membership_verification, client_name=request.user)
            if loan_obj.verification_status == True:
                try:
                    if request.method == 'POST':
                        loan_amount = float(request.POST['loan-amount'])
                        loan_period = int(request.POST['loan-period'])
                        account_name = request.POST['account-name']
                        account_number = request.POST['account-number']
                        bank_name = request.POST['bank-name']
                        purpose_for_loan = request.POST['purpose-for-loan']


                        loan_request_object = loan_request_list.objects.get_or_create(
                            client_name = request.user,
                            loan_amount = loan_amount,
                            loan_period = loan_period,
                            account_name = account_name,
                            account_number = account_number,
                            bank_name = bank_name,
                            purpose_for_loan = purpose_for_loan
                        )

                        if loan_request_object:
                            return redirect('/loanrequestSuccess/')

                except(SyntaxError, SyntaxError, ObjectDoesNotExist):
                    pass

            elif loan_obj.verification_status == False:
                return HttpResponseRedirect('/Membership/pending/') 
            
            
        else:
            return HttpResponseRedirect('/verification-required/')

    except(SyntaxError, SyntaxError, ObjectDoesNotExist):
        pass
    
    context = {

    }
    return render(request, 'loans/loan_requests.html', context=context)


@login_required
def approved_loans(request, *args, **kwargs):

    context = {

    }
    return render(request, 'loans/approved_loans.html', context=context)

