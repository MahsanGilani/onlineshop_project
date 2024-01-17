from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.utils import timezone
import datetime
from django.utils.text import slugify

from apps.products.models import Category

class CategoryModelTest(TestCase):
    
    def setUp(self) -> None:
        self.category1 = Category(category_name='pizza', slug='pizza')
        self.category2 = Category(category_name='fast-food', sub_category=self.category1)
        self.category3 = Category(category_name='sand wich',slug='sand-wich')

    def test_category_creation(self):
        self.assertEqual(str(self.category2), f'{self.category2.category_name}')

    def test_parent_category(self):
        self.assertEqual(self.category2.sub_category, self.category1)

    def test_slug_generation(self):
        self.assertEqual(self.category3.slug, slugify(self.category3))



# class ProductModelTest(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(
#             title='TestCategory',
#         )

#     def test_product_creation(self):
#         product = Product.objects.create(
#             name='TestProduct',
#             short_description='Test short description',
#             price=100.00,
#             category=self.category
#         )
#         self.assertEqual(product.name, 'TestProduct')
#         self.assertEqual(str(product), 'TestProduct')

#     def test_discounted_price(self):
#         product = Product.objects.create(
#             name='TestProduct',
#             short_description='Test short description',
#             price=100.00,
#             discount_type='p',
#             discount_amount=10,
#             category=self.category
#         )
#         self.assertEqual(product.discounted_price, 90)


# class ImageModelTest(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(
#             title='TestCategory',
#         )
#         self.product = Product.objects.create(
#             name='TestProduct',
#             short_description='Test short description',
#             price=100.00,
#             category=self.category
#         )

#     def test_image_creation(self):
#         image_file = SimpleUploadedFile("test_image.jpg", b"test_content", content_type="image/jpeg")
#         image = Image.objects.create(
#             product=self.product,
#             image=image_file
#         )
#         self.assertEqual(str(image), ' تصویرTestProduct')


