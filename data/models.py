from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

class Country(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
  
class Property(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    address = models.CharField(max_length=255)
    building_grade = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, default=0, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    createdon = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, blank=True, null=True)
    modifiedon = models.DateTimeField(auto_now=True)
    modifiedby = models.ForeignKey(User, related_name="property_modified_by", blank=True, null=True)

    def __str__(self):
        return self.name
       
    def get_absolute_url(self):
        return reverse('data:detail', args=(self.pk,))
        
class Stock(models.Model):
    property = models.ForeignKey(Property, db_index=True)
    name = models.CharField(max_length=30)
    floor = models.IntegerField()
    available = models.DateTimeField(blank=True, null=True)
    createdon = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, blank=True, null=True)
    modifiedon = models.DateTimeField(auto_now=True)
    modifiedby = models.ForeignKey(User, related_name="stock_modified_by", blank=True, null=True)

    def __str__(self):
        return self.name
       
    def get_absolute_url(self):
        return reverse('data:detail_stock', args=(self.pk,))

        
fs = FileSystemStorage(location='/media/photos')
        
class Image(models.Model):
    property = models.OneToOneField(Property)
    title = models.CharField(max_length=30)
    image_body = models.ImageField(fs)
    
    def __str__(self):
        return self.title

