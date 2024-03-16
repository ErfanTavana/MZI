from django.db import models
from MZI.models import Base_Model
from django.contrib.auth.models import User


class Certificate(Base_Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='عنوان مدرک')
    image = models.ImageField(upload_to='certificate_images/', null=True, blank=True, verbose_name='عکس مدرک')
    def save(self, *args, **kwargs):
        # حذف فواصل چپ و راست از نام دسته بندی
        self.title = self.title.strip()
        super().save(*args, **kwargs)

