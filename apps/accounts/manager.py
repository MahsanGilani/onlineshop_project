from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from django.contrib.auth.models import UserManager

class LogicalQuerySet(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True)

class LogicalManager(UserManager):
    
    def logical_queryset(self):
        return LogicalQuerySet(self.model)
    
    def get_queryset(self):
        return self.logical_queryset().filter(is_deleted=False)
    
    def archive(self):
        return self.logical_queryset()
    
    def deleted(self):
        return self.logical_queryset().filter(is_deleted=True)
    
    def create_superuser(self, username, email, password, **extra_fields):
        # چون ایز اکتیو رو در حالت دیفالت روی فالس قراردادیم، برای ساخت سوپریوزر بهمون ارور میداد، در نتیجه میایم اینجا از فالس برش میداریم.
        extra_fields.setdefault('is_active', True)
        return super().create_superuser(username, email, password, **extra_fields)