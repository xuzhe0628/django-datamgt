from django.conf.urls import url
from django.contrib.auth import views as auth_views



from datamgt import settings
from . import views

app_name = 'data'
urlpatterns = [
    #General URLConfs
    url(r'^list$', views.ListView.as_view(), name='list'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^password_change/$', auth_views.password_change, {'template_name': 'data/auth/change_password.html', 'post_change_redirect' : 'data:index'}, name='password_change',),
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    #Property URLConfs
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteView.as_view(), name='delete'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateView.as_view(), name='update'),
    url(r'^add/$', views.AddView.as_view(), name='add'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    
    #Stock URLConfs
    url(r'^detail_stock/(?P<pk>[0-9]+)/$', views.DetailViewStock.as_view(), name='detail_stock'),
    url(r'^delete_stock/(?P<pk>[0-9]+)/$', views.DeleteViewStock.as_view(), name='delete_stock'),
    url(r'^update_stock/(?P<pk>[0-9]+)/$', views.UpdateViewStock.as_view(), name='update_stock'),
    url(r'^add_stock/$', views.AddViewStock.as_view(), name='add_stock'),
    url(r'^search_stock/$', views.SearchViewStock.as_view(), name='search_stock'),
    #test URLConfs
    #url(r'^property_autocomplete/$',views.PropertyAutocomplete.as_view(create_field='name'),name='property_autocomplete',),
    url(r'^search_stock/stock_list', views.StockListView.as_view(), name='stock_list'),
    url(r'^search/property_list', views.PropertyListView.as_view(), name='property_list'),
]