from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from ecommerce.views import SearchResultView



app_name = 'ecommerce'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
    path('create/', views.order_create, name='order_create'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('/property-enquiry/', views.property_enquiry, name='property-enquiry')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
