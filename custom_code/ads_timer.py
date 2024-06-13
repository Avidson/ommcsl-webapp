from datetime import datetime 
from django.utils import timezone
from ads import models
from django.shortcuts import render, redirect, get_object_or_404
import sys 

def ads_timer_func(obj1, obj2):
    try:

        format_date1 = obj1.strftime("%Y%m%d%H%M%S")
        format_date2 = obj2.strftime("%Y%m%d%H%M%S")

        new_format1 = int(format_date1)
        new_format2 = int(format_date2)

        time_difference = new_format2 - new_format1

        current_datetime = timezone.now()
        format_current_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

        #model instance
        model_instance_call = Display_ads.objects.filter(approved=True)
    
        new_time_difference = int(format_current_datetime) - int(time_difference)

        if new_time_difference <= 0 :
            model_instance_call = False 
        elif new_time_difference > 0:
            model_instance_call = True
    except:
        print('There was an error while running your code.')

if '__main__' == __name__:
    ads_timer_func()

