from django.shortcuts import render
from ads.models import Display_ads
# Create your views here.



def ads_view(request, *args, **kwargs):

    available_ads = Display_ads.objects.filter(approved=True)
    

    context = {
        'available': available_ads,

    }

    return render(request, '', context=context)