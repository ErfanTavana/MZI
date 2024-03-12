from django.db import models


class Home(models.Model):
    country = models.CharField(blank=True, null=True, max_length=100, verbose_name='کشور')
    province = models.CharField(blank=True, null=True, max_length=100, verbose_name='استان')
    city = models.CharField(blank=True, null=True, max_length=100, verbose_name='شهر')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    full_address = models.TextField(blank=True, null=True, verbose_name='آدرس کامل')
    phone_prefix = models.CharField(blank=True, null=True, max_length=5, verbose_name='پیش‌ شماره')
    phone_number = models.CharField(blank=True, null=True, max_length=15, verbose_name='شماره تلفن')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    working_days = models.CharField(blank=True, null=True, max_length=50, verbose_name='روزهای کاری')
    whatsapp_mz = models.URLField(blank=True, null=True, verbose_name='آدرس واتساپ MZ')
    linkedin_mz = models.URLField(blank=True, null=True, verbose_name='لینکدین MZ')
    instagram_mz = models.URLField(blank=True, null=True, verbose_name='آدرس اینستاگرام MZ')
    telegram_mz = models.URLField(blank=True, null=True, verbose_name='آدرس تلگرام MZ')
    vichat_mz = models.URLField(blank=True, null=True, verbose_name='ویچت MZ')
