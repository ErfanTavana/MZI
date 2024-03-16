from django.db import models
from MZI.models import Base_Model
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class CategoryArticle(Base_Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام دسته بندی')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # حذف فواصل چپ و راست از نام دسته بندی
        self.name = self.name.strip()

        # فراخوانی متد save اصلی
        super().save(*args, **kwargs)
class TagArticle(Base_Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام برچسب')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # حذف فواصل چپ و راست از نام برچسب
        self.name = self.name.strip()

        # فراخوانی متد save اصلی
        super().save(*args, **kwargs)
class Article(Base_Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='عنوان مقاله')
    description = models.TextField(verbose_name='توضیحات مقاله')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True, verbose_name='عکس مقاله')
    categories = models.ManyToManyField(CategoryArticle, related_name='articles', verbose_name='دسته بندی‌ها')
    tags = models.ManyToManyField(TagArticle, related_name='articles', verbose_name='برچسب‌ها')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # حذف فواصل چپ و راست از نام دسته بندی
        self.title = self.title.strip()
        super().save(*args, **kwargs)
@receiver(pre_delete, sender=Article)
def delete_article_files(sender, instance, **kwargs):
    # حذف فایل مرتبط با مقاله
    if instance.image:
        instance.image.delete(save=False)