from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Review
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from cart.form import CartAddProductForm
from django.shortcuts import render
from .models import OrderItem, Order, Property_enquirie
from .forms import OrderCreateForm
from cart.cart import Cart
from main.models import Profile
from ads.models import Display_ads
import requests 
from django.conf import settings 
import json
from ecommerce.tasks import payment_created


api_key = settings.PAYSTACK_SECRETE_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 100) #for paginator to display items on each page
    page = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page_obj = paginator.get_page(paginator.num_pages) 

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    available_ads = Display_ads.objects.filter(approved=True)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page_obj' : page_obj,
        'available_ads' : available_ads,
    }
    return render(request, 'ecommerce/ecommerce.html', context=context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    reviews = product.products.filter(active=True, post_id=id)
    categories = Category.objects.all()
    count_category = Category.objects.filter(slug=slug).count()

    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        body = request.POST['comments']

        new_review = Review.objects.get_or_create(
            post = product,
            name = name,
            email = email,
            body = body
        )

        if new_review:
            review_message = messages.info(request, 'Your review has been posted')

    context = {
        'product' : product,
        'cart_product_form' : cart_product_form,
        'reviews' : reviews, 
        'categories' : categories,
        'count_category' : count_category,
    }

    return render(request, 'ecommerce/productDetail.html', context=context)


class SearchResultView(ListView):

    model = Product
    template_name = 'ecommerce/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(description__icontains=query) | Q(name__icontains=query)
        )
        return object_list


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            #request.session['ecommerce_pay_id'] = OrderItem.id
            #return redirect(reverse("ecommerce:processing-payment" ))
            return render(request, 'ecommerce/create.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'ecommerce/checkout.html', {'cart': cart, 'form': form})

def payment_process(request):

    payment_id = request.session.get('ecommerce_pay_id')
    payment = get_object_or_404(OrderItem, id=payment_id)
    amount = payment.get_amount() * 100
    profile = get_object_or_404(Profile, profile_owner=request.user)

    if request.method == 'POST' :

        success_url = request.build_absolute_uri(
            reverse('inAppDonations:payment-success')
        )
        cancel_url = request.build_absolute_uri(
            reverse('inAppDonations:payment-canceled')
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
            return render(request, 'inApp_donation/process_payment.html', locals())

    else:
        return render(request, 'inApp_donation/process_payment.html', locals())


@login_required
def payment_success(request):
    # retrive the payment_id we'd set in the django session ealier
    payment_id = request.session.get('ecommerce_pay_id', None)#new
    # using the payment_id, get the database object
    payment = get_object_or_404(Order, id=Order.id)

    
    ref = request.GET.get('reference', '')#new
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

            payment_created.delay(payment.pk)

  
    return render(request, 'inApp_donation/payment_success.html', {})

@login_required
def payment_canceled(request):
    return render(request, 'inApp_donation/payment_cancel.html', {})



def property_enquiry(request, *args, **kwargs):

    forms = Property_enquirie(request.POST)

    if request.method == 'POST':

        full_name = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['comments']

        add_message = Property_enquirie.objects.create(
            full_name = full_name,
            phone = phone,
            email = email,
            message = message
        )
        

    context = {

        'forms' : forms,
    }
    return render(request, 'ecommerce/productDetail.html', context=context)