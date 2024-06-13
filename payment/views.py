from django.shortcuts import render, redirect
import json
import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from payment.models import Payment
from django.urls import reverse
from django.contrib import messages
# Create your views here.


api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL



def payment(request, *args, **kwargs):

    form = Payment(request.POST)

    if request.method == 'POST':

        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        payment_type = request.POST['option']
        amount = request.POST['amount']


        new_payment = Payment.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            payment_purpose = payment_type,
            amount = amount,
        )

        request.session['payment_id'] = new_payment.id

        messages.success(request, 'Payment Processing....')

        if new_payment:
            return redirect('payment:process')

    return render(request, 'payment/payment.html', {'form': form})

def payment_process(request, *args, **kwargs):

    payment_id = request.session.get('payment_id', None)

    payment = get_object_or_404(Payment, id=payment_id)

    amount = payment.get_amount() * 100

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('payment:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('payment:payment-canceled')
        )

        metadata = json.dumps({
            "payment_id" : payment_id,
            "cancel_action" : cancel_url,
        })

        context = {
        'email' : payment.email,
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
            return render(request, 'payment/process.html', locals())

    else:
        return render(request, 'payment/process.html', locals())


def payment_success(request, *args, **kwargs):

    # retrive the payment_id we'd set in the django session ealier
    payment_id = request.session.get('payment_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(Payment, id=payment_id)#new

    # retrive the query parameter from the request object
    ref = request.GET.get('reference', '')#new
    # verify transaction endpoint
    url = 'https://api.paystack.co/transaction/verify/{}'.format(ref)#new

    # set auth headers
    headers = {"authorization": f"Bearer {api_key}"}#new
    r = requests.get(url, headers=headers)#new
    res = r.json()#new
    res_ = res['data']

    # verify status before setting payment_ref
    if res_['status'] == "success":  # new
        # update payment payment reference
        if payment:
            payment.paystack_ref = ref #new
            payment.paid = True
            payment.save()#new


    return render(request, 'payment/payment_success.html', {})

def payment_canceled(request):
    return render(request, 'payment/payment_canceled.html', {})



