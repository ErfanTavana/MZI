from django.db import models
from django.contrib.auth.models import User
from MZI.models import Base_Model

class AdminMZI(Base_Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ادمین')
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='نام')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='نام خانوادگی')
    role_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام مسئولیت')
    profile_image = models.ImageField(upload_to='admin_profile_images/', null=True, blank=True, verbose_name='عکس پروفایل')
    def __str__(self):
        return self.user.username