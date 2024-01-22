from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.order'
    verbose_name = _('Order Models List')