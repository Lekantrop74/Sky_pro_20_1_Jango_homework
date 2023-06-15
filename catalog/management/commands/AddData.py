from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Удаление всех записей из таблиц Category и Product
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Список категорий для заполнения базы данных
        category_list = [
            {'name': 'Овощи', 'description': 'Полезные овощи'},
            {'name': 'Фрукты', 'description': 'Вкусные фрукты'}
        ]

        # Создание записей в таблице Category
        for category_item in category_list:
            Category.objects.create(
                name=category_item['name'],
                description=category_item['description']
            )

        # Получаем категории "Овощи" и "Фрукты"
        category_vegetables = Category.objects.get(name='Овощи')
        category_fruits = Category.objects.get(name='Фрукты')

        # Список продуктов для заполнения базы данных
        product_list = [
            {
                'name': 'Морковь',
                'description': 'Сладкая и сочная морковь',
                'preview_image': None,
                'category': category_vegetables,
                'price': 1.99
            },
            {
                'name': 'Картофель',
                'description': 'Отличный компаньон для любой еды',
                'preview_image': None,
                'category': category_vegetables,
                'price': 2.99
            },
            {
                'name': 'Лук',
                'description': 'Прекрасный способ придать пикантность любому блюду',
                'preview_image': None,
                'category': category_vegetables,
                'price': 0.99
            },
            {
                'name': 'Томаты',
                'description': 'Сочные и полные витаминов томаты',
                'preview_image': None,
                'category': category_vegetables,
                'price': 3.99
            },
            {
                'name': 'Огурцы',
                'description': 'Превосходный перекус на горячий день',
                'preview_image': None,
                'category': category_vegetables,
                'price': 2.49
            },
            {
                'name': 'Яблоки',
                'description': 'Cочные и сладкие яблоки, полные витаминов',
                'preview_image': None,
                'category': category_fruits,
                'price': 4.99
            },
            {
                'name': 'Апельсины',
                'description': 'Свежие и кисло-сладкие апельсины',
                'preview_image': None,
                'category': category_fruits,
                'price': 3.49
            },
            {
                'name': 'Груши',
                'description': 'Нежные и сладкие груши',
                'preview_image': None,
                'category': category_fruits,
                'price': 5.99
            },
            {
                'name': 'Бананы',
                'description': 'Eще один прекрасный источник витаминов',
                'preview_image': None,
                'category': category_fruits,
                'price': 2.99
            },
            {
                'name': 'Киви',
                'description': 'Маленький зеленый плод, но как много в нем витаминов!',
                'preview_image': None,
                'category': category_fruits,
                'price': 1.99
            }
        ]

        # Создание записей в таблице Product с помощью bulk_create
        product_bulk_list = []
        for product_item in product_list:
            product_bulk_list.append(Product(
                name=product_item['name'],
                description=product_item['description'],
                preview_image=product_item['preview_image'],
                category=product_item['category'],
                price=product_item['price']
            ))
        Product.objects.bulk_create(product_bulk_list)
