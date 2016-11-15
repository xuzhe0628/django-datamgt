from django.views import generic
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import django.contrib.auth.mixins as mixin
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.contrib.auth.models import User
from dal import autocomplete
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Property, Stock
from .forms import SearchForm, LoginForm, AddForm, UpdateForm, SearchFormStock, AddFormStock, UpdateFormStock

#General Views

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/index.html' 

    def get_queryset(self):
        return
        
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_stock_list'] = Stock.objects.all().order_by("-createdon")[:10]
        context['latest_property_list'] = Property.objects.annotate(num_stocks=Count('stock')).order_by('-num_stocks')[:5]
        return context
        
class ListView(LoginRequiredMixin, generic.ListView):
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/list.html' 

    def get_queryset(self):
        return
        
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['my_stock_list'] = Stock.objects.filter(createdby=self.request.user).order_by("-createdon")
        context['my_property_list'] = Property.objects.filter(createdby=self.request.user).annotate(num_stocks=Count('stock')).order_by('-num_stocks')
        return context
    
class LoginView(generic.edit.FormView):
    template_name = 'data/auth/login.html'
    form_class = LoginForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('data:index')
            else:
                return redirect('data:login')

class StockListView(LoginRequiredMixin, generic.ListView):
    model = Stock
    paginate_by = 5
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/stock_list.html'
    
    def get_queryset(self):
        old_request = self.request.session['old_post']
        result = Stock.objects.filter(property__name__contains=old_request['buildingname']).order_by(old_request['orderby'])
        return result

class PropertyListView(LoginRequiredMixin, generic.ListView):
    model = Property
    paginate_by = 5
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/property_list.html'
    
    def get_queryset(self):
        old_request = self.request.session['old_post']
        result = Property.objects.filter(name__contains=old_request['buildingname']).order_by(old_request['orderby'])
        return result
                
'''                
class LogoutView(LoginRequiredMixin, generic.TemplateView):
    redirect_field_name = 'redirect_to'
    login_url = '/data/login/'
    template_name = 'data/logout.html'
'''

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/data/login/')

#Property Views
class SearchView(LoginRequiredMixin, generic.edit.FormView):
    form_class = SearchForm
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/search.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pat = request.POST['buildingname'].strip()
            order = request.POST['orderby'].strip()
            result = Property.objects.filter(name__contains=pat).order_by(order)
            if result:
                request.session['old_post'] = request.POST
                return HttpResponseRedirect('property_list')
        else:
            return render(request, 'data/search.html', { 'form' : form })

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Property
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['stock_list'] = Stock.objects.filter(property__id=self.kwargs['pk']).order_by("-createdon")
        return context
    
 
class AddView(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.CreateView):
    form_class = AddForm
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/add.html'
    permission_required = 'data.add_property'

class UpdateView(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.UpdateView):
    model = Property
    form_class = UpdateForm
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/update.html'
    permission_required = 'data.change_property'

class DeleteView(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.DeleteView):
    model = Property
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/delete.html'
    success_url = '/data'
    permission_required = 'data.delete_property'

#Stock Views
class SearchViewStock(LoginRequiredMixin, generic.edit.FormView):
    form_class = SearchFormStock
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/search_stock.html'
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pat = request.POST['buildingname'].strip()
            order = request.POST['orderby'].strip()
            result = Stock.objects.filter(property__name__contains=pat).order_by(order)
            if result:
                request.session['old_post'] = request.POST
                return HttpResponseRedirect('stock_list')
        else:
            return render(request, 'data/search_stock.html', { 'form' : form })
    
                
                
class DetailViewStock(LoginRequiredMixin, generic.DetailView):
    model = Stock
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/detail_stock.html' 
 
class AddViewStock(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.CreateView):
    form_class = AddFormStock
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/add_stock.html'
    permission_required = 'data.add_stock'

class UpdateViewStock(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.UpdateView):
    model = Stock
    form_class = UpdateFormStock
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/update_stock.html'
    permission_required = 'data.change_stock'

class DeleteViewStock(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.DeleteView):
    model = Stock
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/delete_stock.html'
    success_url = '/data'
    permission_required = 'data.delete_stock'
    
#View for properrt autocomplete
class PropertyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Country.objects.none()

        qs = Property.objects.all()

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs

'''     
class TestAddStock(LoginRequiredMixin, generic.edit.CreateView):
    model = Stock
    form_class = TestStockForm
    login_url = '/data/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'data/test_add_stock.html'
    
    def get_object(self):
        return Property.objects.first()
'''