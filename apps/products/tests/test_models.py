from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.utils import timezone
import datetime
from django.utils.text import slugify

from apps.products.models import Category, Product

class CategoryModelTest(TestCase):
    
    def setUp(self) -> None:
        self.category1 = Category(category_name='pizza', slug='pizza')
        self.category2 = Category(category_name='fast-food', sub_category=self.category1)
        self.category3 = Category(category_name='sand wich',slug='sand-wich')

    def test_category_creation(self):
        self.assertEqual(str(self.category2), f'{self.category2.category_name}')

    def test_parent_category(self):
        self.assertEqual(self.category2.sub_category, self.category1)

    def test_slug_cat_generation(self):
        self.assertEqual(self.category3.slug, slugify(self.category3))



class ProductModelTest(TestCase):

    def setUp(self) -> None:
        self.product1 = Product(product_name='steak', product_price=800000, product_quantity=5,is_active=True, description='steak is good',slug='steak')
        self.product2 = Product(product_name='shrimp', product_price=900000, product_quantity=20,is_active=True, description='Shrimp is good',slug='shrimp')                                  
        self.product3 = Product(product_name='hot dog', product_price=225000, product_quantity=24,is_active=True, description='Hot Dog is good',slug='hot-dog')   
        self.product4 = Product(product_name='taco', product_price=250000, product_quantity=13,is_active=True, description='Taco is good',slug='taco')
                                               
    def test_product_creation(self):
        self.assertEqual(str(self.product1), f'{self.product1.product_name}')
        self.assertEqual(str(self.product2), f'{self.product2.product_name}')
        self.assertEqual(str(self.product3), f'{self.product3.product_name}')
        self.assertEqual(str(self.product4), f'{self.product4.product_name}')
        
    def test_slug_pro_generation(self):
        self.assertEqual(self.product1.slug, slugify(self.product1))
        self.assertEqual(self.product2.slug, slugify(self.product2))
        self.assertEqual(self.product3.slug, slugify(self.product3))
        self.assertEqual(self.product4.slug, slugify(self.product4))