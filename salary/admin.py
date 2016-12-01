from django.contrib import admin

# Register your models here.
from .models import OfferInfo,OfferMessage


admin.site.register(OfferInfo)
admin.site.register(OfferMessage)