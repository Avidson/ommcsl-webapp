from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from custom_code import pass_code as encrypter
from django.db.models import Q 
from django.forms.models import inlineformset_factory
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from Membership.models import Membership_verification
from wallet.models import TopUp
from django.db.models import Sum
from decimal import Decimal
from main.models import Profile
import json 
import requests 
from . tasks import payment_completed


# Create your views here.

api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL

minimum_balance = 20000

@login_required
def share_holding(request, *args, **kwargs):

    try:

        if Membership_verification.objects.filter(client_name=request.user).exists():
            obj = get_object_or_404(Membership_verification, client_name=request.user)
            
            if obj.verification_status == True:
                context = {}
                return render(request, 'shares/shares_index.html', context=context)

            elif obj.verification_status == False:
                return HttpResponseRedirect('/Membership/pending/') 
            else:
                return HttpResponseRedirect('/verification-required/')

    except SystemError as e:
        print('Error at'.format(e))
        
    context = {

    }

    return render(request, 'shares/shares_index.html', context=context)




@login_required
def send_payment_for_share(request, *args, **kwargs):

    form = Payment_for_Share(request.POST)
    try:
        if request.method == 'POST':
            amount = request.POST['amount']

            new_payment = Payment_for_Share.objects.create(
                client_name = request.user, 
                amount = amount,
            )

            if new_payment:
                request.session['shares_id'] = new_payment.id
                return redirect(reverse("Shares:process" ))
    except:
        pass

    context = { }

    return render(request, 'shares/shares_send_payment.html', context=context)



@login_required
def payment_process(request):

    payment_id = request.session.get('shares_id')
    payment = get_object_or_404(Payment_for_Share, id=payment_id)
    amount = payment.get_amount() * 100
    profile = get_object_or_404(Profile, profile_owner=request.user)

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Shares:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Shares:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'email' : profile.email,
        'amount' : int(amount),
        'callback_url' : success_url,
        'metadata' : metadata,
         }

        headers = {"authorization" : f"Bearer {api_key}"}

        r = requests.post(url, headers=headers, data=context)
        response = r.json()

        if response['status'] == True:
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass 
        else:
            return render(request, 'wallet/process_payment.html', locals())

    else:
        return render(request, 'wallet/process_payment.html', locals())


@login_required
def payment_success(request):
    
    payment_id = request.session.get('shares_id', None)
    payment = get_object_or_404(Payment_for_Share, client_name=request.user)

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}
    r = requests.get(url, headers=headers)
    res = r.json()
    res_ = res["data"]

    if res_['status'] == "success":  
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref
            payment.save()

            payment_completed.delay(payment.pk)

    return render(request, 'wallet/payment_success.html', {})

@login_required
def payment_canceled(request):
    return render(request, 'wallet/payment_cancel.html', {})


@login_required
def withdrawal_request(request, *args, **kwargs):
    
    context = {}
    return render(request, 'shares/withdrawal.html', context=context)


@login_required
def shares_detail_view(request, *args, **kwargs):
    
    context = {}
    return render(request, 'shares/shares_detail.html', context=context)



