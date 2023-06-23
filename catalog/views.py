from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Contact, Product


# Create your views here.
def home_page(request):
    return render(request, 'catalog/home_page.html')


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return redirect('contact')

    contacts = Contact.objects.order_by('-id')
    return render(request, 'catalog/contact.html', {'contacts': contacts})


def base(request):
    return render(request, 'catalog/base.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
