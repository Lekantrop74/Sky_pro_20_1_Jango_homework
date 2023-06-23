from django.urls import path
from catalog.views import index, contact, home_page, base
from .views import ProductListView








urlpatterns = [
    path('home', index),
    path('contact/', contact, name='contact'),
    path('base/', base),
    path('', ProductListView.as_view(), name='product_list'), # здесь
]
