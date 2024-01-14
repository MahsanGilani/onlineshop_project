from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(verbose_name=_('category_image'), upload_to='categories_img/', height_field=None,
                                       width_field=None)
    sub_category_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories')
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.category_name
