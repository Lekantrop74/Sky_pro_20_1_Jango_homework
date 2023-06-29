from django.urls import path
from django.views.generic import RedirectView

from catalog.views import index, contact, home_page, product_list, add_data, ContactCreateView

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('', RedirectView.as_view(url='/home_page/', permanent=True)),
    path('index/', index, name='index'),
    path('contact_page/contact/', contact, name='contact'),
    path('create/', ContactCreateView.as_view(), name='create_contact'),
    path('base/',  product_list, name='product_list_base'),
    path('base/add_data/', add_data, name='add_data'),
]