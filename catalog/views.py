from django.core.paginator import Paginator


from .models import Contact, Product, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost


# Create your views here.
def home_page(request):
    # Отображение домашней страницы
    return render(request, 'catalog/base_page/home_page.html')


def index(request):
    # Отображение индексной страницы
    return render(request, 'catalog/base_page/index.html')


def navbar(request):
    # Отображение навигационной панели
    return render(request, 'catalog/base_page/navbar.html')


class ContactListView(ListView):
    model = Contact
    template_name = 'catalog/contact_page/contact.html'
    context_object_name = 'contacts'
    ordering = ['-id']
    paginate_by = 5


def contact(request):
    contact_list_view = ContactListView.as_view()
    # Обработчик запроса для страницы контактов
    return contact_list_view(request)


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'email', 'message')
    success_url = reverse_lazy('contact')


class AddDataView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview_image', 'category', 'price')
    template_name = 'catalog/product_page/product_add_data.html'
    success_url = '/base'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # Получение всех категорий товаров и добавление их в контекст
        return context


def base(request):
    # Отображение базовой страницы продуктов
    return render(request, 'catalog/product_page/product_base.html')


class ProductListView(ListView):
    model = Product
    paginate_by = 5
    template_name = 'catalog/product_page/product_list.html'
    context_object_name = 'page_obj'

    def get_queryset(self):
        return Product.objects.order_by('-created_at')
        # Получение списка продуктов, отсортированных по убыванию даты создания

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Paginator(self.get_queryset(), self.paginate_by).get_page(self.request.GET.get('page'))
        # Добавление пагинированного списка продуктов в контекст
        return context





class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_page/blog_base.html'
    context_object_name = 'blog_posts'
    ordering = ['-created_at']
    paginate_by = 5


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog_post_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_update.html'
    context_object_name = 'blog_post'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('blog_post_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    context_object_name = 'blog_post'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('blog_post_list')


def blog_post_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'catalog/blog_page/blog_post_detail.html', {'blog_post': blog_post})

# def product_list(request):
#     # стандартная пагинация не удалил чтобы не искать потом код если нужно будет сделать не через классы
#     products = Product.objects.all()
#     paginator = Paginator(products, 5)  # Разбиваем список на страницы по 5 объектов на каждой
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'catalog/product_page/product_list.html', {'page_obj': page_obj})
