from django.shortcuts import render
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import requests
import json
from main.models import Profile
from . tasks import payment_completed
# Create your views here.

#PAYMENT GATEWAY API CREDENTIALS
api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL


@login_required
def januaryDue(request, *args, **kwargs):

    try:

        if request.method == 'POST' :
            amount = request.POST['amount']

            monthly_payment = JanuaryDue.objects.create( 
                client_name = request.user,
                amount = amount
                 )

            if monthly_payment:
                request.session["payment_id"] = monthly_payment.id
                return redirect(reverse("Monthly_due:payment-process"))

    except SystemError as e:
        pass
    january_payment = JanuaryDue.objects.filter(client_name=request.user, paid=True)

    context = {'january_payment': january_payment}
    return render(request, 'monthly_due/january.html', context=context)

#January payment session
@login_required
def payment_process(request):

    payment_id = request.session.get('payment_id')
    payment = get_object_or_404(JanuaryDue, id=payment_id)
    amount = payment.get_amount() * 100

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('Monthly_due:payment-cancelled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'email': payment.email,
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
                print('There was an error code') 
        else:
            return render(request, 'monthly_due/process_payment.html', locals())

    else:
        return render(request, 'monthly_due/process_payment.html', locals())


@login_required
def payment_success(request):
    
    # retrive the payment_id we'd set in the django session ealier
    payment_id = request.session.get('payment_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(JanuaryDue, client_name=request.user)#new

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

            payment_completed.delay(payment.pk)

  
    return render(request, 'monthly_due/payment_success.html', {})


@login_required
def payment_canceled(request):
    return render(request, 'monthly_due/payment_cancel.html', {})


def month_indexview(request, *args, **kwargs):
    context = {}
    return render(request, 'monthly_due/home.html', context=context)