from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from ecommerce.models import Product
from .cart import Cart
from .form import CartAddProductForm
import json
from django.contrib import messages
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


@require_POST
def cart_add(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')

    except ObjectDoesNotExist:
        return redirect('ecommerce:product_list')
    
        #message = messages.info(request, 'There was an error')
        #return('ecommerce:product_list')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')



def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print(item)
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
        
    return render(request, 'ecommerce/cart.html', {'cart': cart})