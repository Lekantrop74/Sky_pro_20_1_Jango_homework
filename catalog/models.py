from django.db import models


# Create your models here.

class Category(models.Model):
    # name (CharField) - наименование категории
    name = models.CharField(max_length=255, verbose_name="Наименование")
    # description (TextField) - описание категории
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('id',)


class Product(models.Model):
    # name (CharField) - наименование продукта
    name = models.CharField(max_length=255, verbose_name="Наименование")
    # description (TextField) - описание продукта
    description = models.TextField(verbose_name="Описание")
    # preview_image (ImageField) - изображение продукта для отображения в каталоге или на странице продукта
    preview_image = models.ImageField(upload_to='product_images/', verbose_name="Изображение продукта", blank=True,
                                      null=True)
    # category (ForeignKey) - связь с моделью Category, для указания в какой категории находится продукт
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    # price (DecimalField) - цена за покупку продукта
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    # created_at (DateTimeField) - дата и время создания записи
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # updated_at (DateTimeField) - дата и время последнего обновления записи
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('id',)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, unique=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/', verbose_name="Превью", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ('-created_at',)
