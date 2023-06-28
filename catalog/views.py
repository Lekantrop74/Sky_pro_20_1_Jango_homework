from django.core.paginator import Paginator
from .models import Contact, Product, Category
from django.shortcuts import render, redirect


# Create your views here.
def home_page(request):
    return render(request, 'catalog/home_page.html')


def index(request):
    return render(request, 'catalog/index.html')


def get_contacts(x=None):
    contacts = Contact.objects.order_by('-id')[:x]
    context = {
        'contacts': contacts
    }
    return context


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Создаем новый объект Contact с данными из формы
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return redirect('/contact')

    return render(request, 'catalog/contact.html', get_contacts(5))


def contact_output(request):
    return render(request, 'catalog/contact_output.html')


def add_data(request):
    if request.method == 'POST':
        # Retrieve the form data from the POST request
        name = request.POST.get('name')
        description = request.POST.get('description')
        preview_image = request.FILES.get('preview_image')
        category_id = request.POST.get('category')
        price = request.POST.get('price')

        # Create a new Product instance with the retrieved data
        product = Product(
            name=name,
            description=description,
            preview_image=preview_image,
            category_id=category_id,
            price=price
        )

        # Save the product to the database
        product.save()

        # Redirect to a success page or a different URL
        return redirect('/base')  # Replace 'success_page' with your desired URL name

    # If it's a GET request or there are validation errors, render the form template
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'catalog/add_data.html', context)


def base(request):
    return render(request, 'catalog/base.html')


def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)  # Разбиваем список на страницы по 5 объектов на каждой

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/product_list.html', {'page_obj': page_obj})
