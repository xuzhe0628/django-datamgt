from django.contrib import admin

from .models import Property, Country, Stock, Image

admin.site.register(Property)
admin.site.register(Country)
admin.site.register(Stock)
admin.site.register(Image)