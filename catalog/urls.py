from django.urls import path
from django.views.generic import RedirectView

from catalog.views import index, contact, home_page, ContactCreateView, AddDataView, ProductListView, navbar
from . import views
from .views import (
    BlogPostListView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
    blog_post_detail,
)

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('', RedirectView.as_view(url='/home_page/', permanent=True)),
    path('navbar/', navbar, name='navbar'),

    path('index/', index, name='index'),
    path('contact_page/contact/', contact, name='contact'),
    path('create/', ContactCreateView.as_view(), name='create_contact'),
    path('base/product_add_data/', AddDataView.as_view(), name='add_data'),
    path('base/', ProductListView.as_view(), name='product_list_base'),

    path('blog_page/blog_base/', BlogPostListView.as_view(), name='blog_base_page'),
    # path('blog_page/blog_post_detail/', blog_post_detail, name='blog_post_detail'),

    path('create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog_page/blog_post_detail/<slug:slug>/', blog_post_detail, name='blog_post_detail'),

    path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog_page/blog_base/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
]

