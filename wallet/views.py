from django.shortcuts import render
from wallet.models import TopUp
from django.shortcuts import render
from django.shortcuts import render, redirect
import json 
import requests 
from django.conf import settings 
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Profile
from decimal import Decimal
# Create your views here.



api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL


from urllib.parse import urlencode


@login_required
def topup_wallet(request):

    form = TopUp(request.POST)
    
    try:
        if request.method == 'POST':
            amount = request.POST['amount']

            #appending the amount to our profiles account_balance
            
            user_profile = Profile.objects.get(profile_owner=request.user)
            user_profile.account_balance += Decimal(amount)
            user_profile.save()

            new_payment = TopUp.objects.create(
                    client_name = request.user, 
                    amount = amount,
                )

            if new_payment:
                request.session['topup_id'] = new_payment.id
                return redirect(reverse("wallet:process" ))

    except ObjectDoesNotExist as e:
        print('an error at'.format(e))

    return render(request, 'wallet/payment.html', {'form': form})


@login_required
def payment_process(request):

    payment_id = request.session.get('topup_id')
    payment = get_object_or_404(TopUp, id=payment_id)
    amount = payment.get_amount() * 100
    profile = get_object_or_404(Profile, profile_owner=request.user)

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('wallet:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('wallet:payment-canceled')
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
    
    # retrive the payment_id we'd set in the django session ealier
    payment_id = request.session.get('topup_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(TopUp, client_name=request.user)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res["data"]

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        if payment:
            # update payment payment reference
            payment.paid = True 
            payment.payment_ref = ref #new
            payment.save()#new

            #if payment.paid == True:
            #    user_profile = Profile.objects.get(profile_owner=request.user)
            #    user_profile.account_balance + payment.amount
            #    user_profile.save()

  
    return render(request, 'wallet/payment_success.html', {})

@login_required
def payment_canceled(request):
    return render(request, 'wallet/payment_cancel.html', {})



