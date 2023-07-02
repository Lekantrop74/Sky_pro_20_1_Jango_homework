from django.core.paginator import Paginator
from django.template.defaultfilters import slugify
from unidecode import unidecode

from .forms import BlogPostFilterForm, BlogPostForm
from .models import Contact, Product, Category
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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
    """
    Класс представления для списка блогов.
    Отображает список блогов и позволяет фильтровать их по параметру is_published.
    """
    model = BlogPost
    template_name = 'catalog/blog_page/blog_base.html'
    context_object_name = 'blog_posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """
        Добавляет форму фильтрации блогов в контекст страницы.
        """
        context = super().get_context_data(**kwargs)
        context['filter_form'] = BlogPostFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        """
        Возвращает отфильтрованный queryset блогов в зависимости от параметра is_published.
        """
        queryset = super().get_queryset()
        is_published = self.request.GET.get('is_published')

        if is_published:
            queryset = queryset.filter(is_published=True)

        return queryset


class BlogPostCreateView(CreateView):
    """
    Класс представления для создания блога.
    Отображает форму создания блога и сохраняет данные блога при успешной валидации формы.
    """
    model = BlogPost
    template_name = 'catalog/blog_page/blog_post_create.html'
    success_url = reverse_lazy('blog_base_page')
    form_class = BlogPostForm

    def form_valid(self, form):
        """
        Проверяет валидность формы и сохраняет данные блога.
        Генерирует уникальный slug на основе заголовка блога и устанавливает количество просмотров в 0.
        """
        instance = form.save(commit=False)
        title = instance.title
        slug = slugify(unidecode(title))
        if BlogPost.objects.filter(slug=slug).exists():
            form.errors['title'] = form.error_class(['Блог с таким названием уже существует.'])
            return self.form_invalid(form)
        instance.slug = slug

        views_count = self.request.POST.get('views_count', '')
        instance.views_count = int(views_count) if views_count else 0

        instance.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    """
    Класс представления для обновления блога.
    Отображает форму обновления блога и сохраняет измененные данные блога при успешной валидации формы.
    """
    model = BlogPost
    template_name = 'catalog/blog_page/blog_post_update.html'
    context_object_name = 'blog_post'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    form_class = BlogPostForm

    def form_valid(self, form):
        """
        Проверяет валидность формы и сохраняет измененные данные блога.
        Устанавливает автора блога на текущего пользователя.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Возвращает URL для перенаправления после успешного обновления блога.
        """
        return reverse_lazy('blog_post_detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    """
    Класс представления для удаления блога.
    Отображает подтверждающий экран удаления блога и удаляет блог при подтверждении.
    """
    model = BlogPost
    template_name = 'catalog/blog_page/blog_delete.html'
    context_object_name = 'blog_post'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('blog_base_page')


class BlogPostDetailView(DetailView):
    """
    Класс представления для детального просмотра блога.
    Отображает полную информацию о блоге и увеличивает счетчик просмотров при каждом просмотре.
    """
    model = BlogPost
    template_name = 'catalog/blog_page/blog_post_detail.html'
    context_object_name = 'blog_post'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        """
        Увеличивает счетчик просмотров блога при каждом просмотре.
        """
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


# def product_list(request):
#     # стандартная пагинация не удалил чтобы не искать потом код если нужно будет сделать не через классы
#     products = Product.objects.all()
#     paginator = Paginator(products, 5)  # Разбиваем список на страницы по 5 объектов на каждой
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'catalog/product_page/product_list.html', {'page_obj': page_obj})