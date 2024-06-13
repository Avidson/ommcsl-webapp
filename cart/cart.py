from django.conf import settings
from ecommerce.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from custom_code.decimal_serializer import decimal_serializer


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        try:
            product_id = str(product.id)
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            if override_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity
            self.save()
            
        except ObjectDoesNotExist:
            print('There was an error with execution')

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True
    
   
    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the datasettings...
        """
        try:
            product_ids = self.cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            cart = self.cart.copy()
            for product in products:
                cart[str(product.id)]['product'] = product
                print(cart)
            for item in cart.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                serialized_object = json.dumps(item['total_price'], default=decimal_serializer)
                print('yielded result...')
                yield serialized_object

        except ObjectDoesNotExist:
            pass

    #Number of items in the cart
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()