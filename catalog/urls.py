from django.urls import path
from django.views.generic import RedirectView

from catalog.views import index, contact, home_page, ContactCreateView, AddDataView, ProductListView, navbar, \
    BlogPostDetailView, ProductDetailView, ProductUpdateView, ProductPostDeleteView
from .views import (
    BlogPostListView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
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
    path('base/product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('base/product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('base/product_delete/<int:pk>/', ProductPostDeleteView.as_view(), name='product_delete'),

    path('blog_page/blog_base/', BlogPostListView.as_view(), name='blog_base_page'),
    path('blog_page/blog_post_detail/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog_page/blog_base/<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog_page/blog_base/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('blog_page/blog_base/blog_post_create', BlogPostCreateView.as_view(), name='blog_post_create'),

]
