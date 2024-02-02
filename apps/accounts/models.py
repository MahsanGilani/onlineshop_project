from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from apps.accounts.manager import LogicalManager
from django.conf import settings
from apps.accounts.validators import validate_birthday

class CustomerUser(BaseModel, AbstractUser):

    # Choices Class
    class UserRole(models.TextChoices):
        CUSTOMERUSER_EMPLOYEE = 'EM', 'Employee'
        CUSTOMERUSER_CUSTOMER = 'CU', 'Customer'
        CUSTOMERUSER_MANAGER = 'MA', 'Manager'

    class GenderChoice(models.TextChoices):
        USER_WOMAN = 'W', 'Woman'
        USER_MAN = 'M', 'Man'

    # Validators
    mobile_regex = RegexValidator(regex='^(\+98|0)?9\d{9}$', message="Phone number must be entered in the format: '+989199999933' or '09199999999'.")
    
    # data fields
    first_name = models.CharField(verbose_name=_('First Name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=45, null=True, blank=True)
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    phone_number = models.CharField(verbose_name=_('Phone Number'), validators=[mobile_regex], max_length=13, unique=True)
    
    birthday = models.DateField(verbose_name=_('Birthday'), validators=[validate_birthday], null=True, blank=True)
    user_role = models.CharField(verbose_name=_('User Role'), max_length=2, choices=UserRole.choices, default=UserRole.CUSTOMERUSER_CUSTOMER)
    
    gender = models.CharField(verbose_name=_('Gender'),max_length=1, choices=GenderChoice.choices, default=GenderChoice.USER_WOMAN)
    
    national_code = models.CharField(verbose_name=_('National Code'), max_length=10, null=True, blank=True, unique=True)
    
    user_image = models.ImageField(verbose_name=_('User Image'),upload_to='user_img/', height_field=None, width_field=None, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Is Active?'), default=False)
    is_staff = models.BooleanField(verbose_name=_('Is Staff?'), default=False)
    
    # USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ('email', 'phone_number')

    objects = LogicalManager()
    
    class Meta:
        ordering = ('first_name',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        # indexes, improves the speed of searches and filters related to that model in the database.
        indexes = [
            models.Index(fields=['first_name']),
        ]
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        # return f'{self.email}'
        return self.full_name()
    
    # دیلیت های تک آبجکته
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
        
    def undelete(self):
        self.is_deleted = False
        self.save()
        

class Address(models.Model):
    # data fields
    postal_code = models.CharField(verbose_name=_('Postal Code'), max_length=10)
    country = models.CharField(verbose_name=_('Country'), max_length=50, default='Iran')
    province = models.CharField(verbose_name=_('Province'), max_length=50)
    city = models.CharField(verbose_name=_('City'), max_length=50)
    main_street = models.CharField(verbose_name=_('Main Street'), max_length=50)
    address_detail = models.TextField(verbose_name=_('Address Deatail'))
    house_number = models.CharField(verbose_name=_('House Number'), max_length=4)
    
    
    # foreignkey
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Customer'))
    
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
    
    def __str__(self) -> str:
        return f'{self.city}-{self.main_street}-->{self.address_detail}'