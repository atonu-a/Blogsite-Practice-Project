from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True #eta use korle model ta db te jabe na
        
# Create your models here.
