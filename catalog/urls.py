from django.urls import path
from catalog.views import index, contact, home_page


urlpatterns = [
    path('', home_page),
    path('home', index),
    path('contact/', contact, name='contact')
]