from django.db import models
from custom_code.ads_timer import ads_timer_func
from django.utils import timezone

# Create your models here.

class Display_ads(models.Model):
    ads_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    organisation_name = models.CharField(max_length=200)
    ads_url = models.URLField(max_length=200, default=None)
    ads_starts = models.DateTimeField()
    ads_end = models.DateTimeField() 
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return self.organisation_name

#    def save(self, *args, **kwargs):
#        current_datetime = timezone.now()
#        format_current_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
#        ad_start = self.ads_starts
#        ad_end = self.ads_end
#        timing = ads_timer_func(ad_start, ad_end)
#        
#        if timing <= 0:
#            self.approved = False
#        elif timing > 0:
#            self.approved = True
#        super(Display_ads, self).save(*args, **kwargs) 
