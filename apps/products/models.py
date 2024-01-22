from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from apps.core.models import BaseModel


# Manger
class ProductManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# Models
class Category(BaseModel):
    # data fields
    category_name = models.CharField(max_length=100, verbose_name=_('Category Name'))
    category_image = models.ImageField(verbose_name=_('Category image'), upload_to='categories_img/', height_field=None,
                                       width_field=None, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=250, unique=True, blank=True, allow_unicode=True)

    # relations
    sub_category = models.ForeignKey('self', verbose_name=_('Sub Categories'), on_delete=models.CASCADE,
                                     related_name='sub_categories', null=True, blank=True)

    class Meta:
        ordering = ('category_name',)  # It does not apply anything to the database
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # indexes, improves the speed of searches and filters related to that model in the database.
        indexes = [
            models.Index(fields=['category_name']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(BaseModel):
    # data fields
    product_name = models.CharField(max_length=150, verbose_name=_('Product Name'))
    product_price = models.PositiveIntegerField(verbose_name=_('Product Price'))
    product_quantity = models.PositiveIntegerField(verbose_name=_('Product Quantity'))
    product_discount = models.PositiveIntegerField(verbose_name=_('Product Discount'), null=True, blank=True)
    discount_valid_from = models.DateField(verbose_name=_('Discount Valid From'), null=True, blank=True)
    discount_valid_to = models.DateField(verbose_name=_('Discount Valid To'), null=True, blank=True)
    video = models.FileField(upload_to='videos/', verbose_name=_('Product Video'), null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Is Active'))
    description = models.TextField(verbose_name=_('Product Description'), null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=250, unique=True, blank=True, allow_unicode=True)
    thumbnail = models.ImageField(verbose_name=_('Product thumbnail'), upload_to='product_img/', height_field=None,
                                  width_field=None, null=True, blank=True)

    # relations
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True,
                                 blank=True)  # null is for database, blank is for panel

    # manager
    objects = models.Manager()
    actives = ProductManger()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('product_name',)  # It does not apply anything to the database
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        # indexes, improves the speed of searches and filters related to that model in the database.
        indexes = [
            models.Index(fields=['product_name']),
        ]
        default_manager_name = 'actives'

    def __str__(self):
        return self.product_name


class Images(BaseModel):
    # data fields
    image = models.ImageField(verbose_name=_('Product thumbnail'), upload_to='product_img/', height_field=None,
                              width_field=None)
    # relations
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='image_products', null=True)
