from django.urls import path
from django.views.generic import RedirectView

from catalog.views import index, contact, home_page, ContactCreateView, AddDataView, ProductListView, navbar

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('', RedirectView.as_view(url='/home_page/', permanent=True)),
    path('navbar/', navbar, name='navbar'),

    path('index/', index, name='index'),
    path('contact_page/contact/', contact, name='contact'),
    path('create/', ContactCreateView.as_view(), name='create_contact'),
    path('base/product_add_data/', AddDataView.as_view(), name='add_data'),
    path('base/', ProductListView.as_view(), name='product_list_base'),

]