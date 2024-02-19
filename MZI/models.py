from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import string
import random
from rest_framework.authtoken.models import Token


def generate_complex_id():
    id_length = 8
    characters = string.ascii_letters + string.digits
    complex_id = ''.join(random.choice(characters) for _ in range(id_length))
    return complex_id


class Base_Model(models.Model):
    id = models.CharField(primary_key=True, default=generate_complex_id, max_length=10, editable=False,
                          verbose_name='شناسه')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='آخرین به‌روزرسانی')
    deleted_at = models.DateTimeField(default=None, null=True, blank=True, verbose_name='تاریخ حذف')
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='deleted_by_%(class)s_set')
    is_ok = models.BooleanField(default=True, verbose_name='آیا تایید شده است؟')
    is_changeable = models.BooleanField(default=True, verbose_name='قابل تغییر است؟')

    class Meta:
        abstract = True

    def soft_delete(self, deleted_by):
        self.deleted_at = timezone.now()
        self.is_ok = False
        self.is_changeable = False
        self.deleted_by = deleted_by
        self.save()
