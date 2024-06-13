from django.db import models
# Create your models here.
from django.urls import reverse
from django.conf import settings
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('ecommerce:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount_available = models.BooleanField(default=False)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image2 = models.FileField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.FileField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ecommerce:product_detail', args=[self.id, self.slug])


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity


class Review(models.Model): 
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=200, default='None')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ecommerce:product_detail', kwargs = {'pk' : self.pk})


class Property_enquirie(models.Model):
    full_name = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    message = models.TextField()

    def __str__(self):
        return self.full_name


