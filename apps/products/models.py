from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name=_('Category Name'))
    category_image = models.ImageField(verbose_name=_('Category image'), upload_to='categories_img/', height_field=None,
                                       width_field=None)
    sub_category = models.ForeignKey('self', verbose_name=_('Sub Categories'), on_delete=models.CASCADE,
                                     related_name='sub_categories')
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        # indexes, improves the speed of searches and filters related to that model in the database.
        indexes = [
            models.Index(fields=['category_name']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
