from django.db import models
from apps.accounts.models import CustomerUser, Address
from apps.products.models import Product
from apps.core.models import BaseModel
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.




class Order(BaseModel):
    # Choices Class
    class StatusMode(models.TextChoices):
        ORDER_STATUS_PAID = 'p', 'Paid'
        ORDER_STATUS_UNPAID = 'u', 'UnPaid'
        ORDER_STATUS_CANCELLED = 'c', 'Cancelled'
    
    # data fields
    status = models.CharField(verbose_name=_('Order Status'),max_length=1, choices=StatusMode.choices, default=StatusMode.ORDER_STATUS_UNPAID)
    total_price = models.PositiveIntegerField(verbose_name=_('Total Price'))
    total_quantity = models.PositiveIntegerField(verbose_name=_('Total Quantity'))
    
    # foreignkey
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'), related_name='orders_users')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name=_('Address'), related_name='orders_address', null=True, blank=True)
    
    
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
    
    
# class OrderItem(BaseModel):
#     # data fields
#     quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
#     total_price = models.PositiveIntegerField(verbose_name=_('Total Price'))