from django.urls import path
from django.views.generic import RedirectView

from catalog.views import index, contact, home_page, product_list, product_list_input, add_data

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('', RedirectView.as_view(url='/home_page/', permanent=True)),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('base/',  product_list, name='product_list_base'),
    path('product_list_input/', product_list_input, name='product_list_input'),
    path('base/add_data/', add_data, name='add_data'),
]
