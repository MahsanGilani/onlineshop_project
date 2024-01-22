from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

# Create your models here.
class BaseModel(models.Model):
    # data fields
    created_at = jmodels.jDateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = jmodels.jDateTimeField(verbose_name=_('Updated at'), auto_now=True)
    is_deleted = models.BooleanField(verbose_name=_('Is deleted'), default=False)
    deleted_at = jmodels.jDateTimeField(verbose_name=_('Deleted at'), blank=True, null=True)
    restored_at = jmodels.jDateTimeField(verbose_name=_('Restored at'), blank=True, null=True)

    
    # Manager
    objects = jmodels.jManager()
    
    
    class Meta:  # can't create instance object from this class
        abstract = True

    # def delete(self, *args, **kwargs):  # logical delete
    #     """
    #         Override Delete Method to Logical Delete Save the Record without Show
    #     """
    #     self.is_deleted = True
