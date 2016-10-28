from django import forms
from django.urls import reverse
from dal import autocomplete

from .models import Property, Stock, Country

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
#Property Forms
class SearchForm(forms.Form):
    OrderByChoice = (
        ('name','Name'),
        ('createdon','Created Time'),
        ('modifiedon','Modified Time')
    )
    buildingname = forms.CharField(label='Building Name')
    orderby = forms.ChoiceField(choices=OrderByChoice, label='Order By')

    
class AddForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ['name', 'address', 'building_grade', 'latitude', 'longitude', 'description', 'country']

        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'building_grade', 'latitude', 'longitude', 'description', 'country']
        
#Stock Forms
class SearchFormStock(forms.Form):
    OrderByChoice = (
        ('name','Name'),
        ('createdon','Created Time'),
        ('modifiedon','Modified Time')
    )
    buildingname = forms.CharField(label='Building Name')
    orderby = forms.ChoiceField(choices=OrderByChoice, label='Order By')
    
    
class AddFormStock(forms.ModelForm):
    
    class Meta:
        model = Stock
        fields = ('name', 'floor', 'available', 'property',)
        widgets = { 'property': autocomplete.ModelSelect2(url='property_autocomplete'), }
        
    def __init__(self, *args, **kwargs):
        super(AddFormStock, self).__init__(*args, **kwargs)
    
    '''
    def clean_property_search(self):
        clean_property_search = self.cleaned_data.get("property_search")
        existing = Property.objects.filter(name=clean_property_search).exists()
        if existing:
            form_property = Property.objects.get(name=self.cleaned_data.get("property_search"))

        if not existing:
            raise forms.ValidationError(u"Property Not Existing. Please create one or search a existing one.")

        return clean_property_search
        
    def save(self):
        temp_stock = super(AddFormStock, self).save(commit=False)
        temp_stock.property = Property.objects.get(name=self.cleaned_data.get("property_search"))
        temp_stock.save()
    '''
        
class UpdateFormStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'property', 'floor', 'available']

'''
#test form for autocomplete
class TestStockForm(autocomplete.FutureModelForm):

    class Meta:
        model = Stock
        fields = ('name', 'floor', 'available', 'property',)
        widgets = { 'property': autocomplete.ModelSelect2(url='property_autocomplete'), }
'''