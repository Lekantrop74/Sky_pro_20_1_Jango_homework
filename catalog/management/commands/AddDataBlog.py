from django.core.management.base import BaseCommand

from catalog.models import BlogPost


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаление всех записей из таблицы BlogPost
        BlogPost.objects.all().delete()

        # Список данных для заполнения базы данных
        blog_post_list = [
            {
                'title': 'Морковь',
                'slug': 'morkov',
                'content': 'Морковь является оранжевым корнеплодом, богатым бета-каротином и другими питательными '
                           'веществами. Она используется в приготовлении салатов, супов и других блюд.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Картофель',
                'slug': 'kartofel',
                'content': 'Картофель является клубнеплодом, который широко используется в кулинарии. Он богат '
                           'крахмалом и является источником энергии. Картофель используется в приготовлении пюре, '
                           'жареных картофелин и других блюд.',
                'preview': 'blog_previews/Картошка.png',
                'is_published': True,
                'views_count': 0
            },
            {
                'title': 'Лук',
                'slug': 'luk',
                'content': 'Лук является овощем с характерным запахом и вкусом. Он используется в приготовлении '
                           'многих блюд, включая супы, соусы и салаты.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Томаты',
                'slug': 'tomaty',
                'content': 'Томаты являются сочным и ароматным фруктом. Они бывают разных сортов, форм и цветов. '
                           'Томаты широко используются в приготовлении салатов, соусов, соков и других блюд.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Огурцы',
                'slug': 'ogurcy',
                'content': 'Огурцы являются освежающим и полезным овощем. Они содержат много воды и являются '
                           'низкокалорийным продуктом. Огурцы часто используются в салатах и закусках.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Яблоки',
                'slug': 'yabloki',
                'content': 'Яблоки являются популярным фруктом с ярким вкусом. Они богаты витаминами и пищевыми '
                           'волокнами. Яблоки можно есть свежими или использовать для приготовления компотов, '
                           'пирогов и других десертов.',
                'preview': 'blog_previews/Яблоко.jpg',
                'is_published': True,
                'views_count': 0
            },
            {
                'title': 'Апельсины',
                'slug': 'apelsiny',
                'content': 'Апельсины являются сочными цитрусовыми фруктами. Они богаты витамином C и другими '
                           'питательными веществами. Апельсины можно есть свежими, соками или использовать для '
                           'приготовления десертов.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Груши',
                'slug': 'grushi',
                'content': 'Груши являются сладкими и сочными фруктами. Они богаты питательными веществами и '
                           'клетчаткой. Груши можно есть свежими или использовать для приготовления компотов, '
                           'салатов и других блюд.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Бананы',
                'slug': 'banany',
                'content': 'Бананы являются питательными и энергетическими фруктами. Они богаты калием и витамином '
                           'B6. Бананы можно есть свежими, использовать в коктейлях, выпечке и других десертах.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            },
            {
                'title': 'Киви',
                'slug': 'kivi',
                'content': 'Киви является экзотическим фруктом с необычной внешностью. Оно имеет зеленую кожуру и '
                           'мягкую сердцевину с множеством мелких семечек. Киви содержит много витамина C и '
                           'клетчатки, которые полезны для иммунной системы и пищеварения.',
                'preview': None,
                'is_published': False,
                'views_count': 0
            }
        ]

        # Создание записей в таблице BlogPost
        BlogPost.objects.bulk_create([
            BlogPost(
                title=item['title'],
                slug=item['slug'],
                content=item['content'],
                preview=item['preview'],
                is_published=item['is_published'],
                views_count=item['views_count']
            ) for item in blog_post_list
        ])