from django.db import models
from MZI.models import Base_Model
from Article.models import CategoryArticle, TagArticle
from django.contrib.auth.models import User


class Portfolio(Base_Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='عنوان نمونه کار')
    description = models.TextField(verbose_name='توضیحات نمونه کار')
    image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True, verbose_name='عکس نمونه کار')
    categories = models.ManyToManyField(CategoryArticle, related_name='portfolio_categories',
                                        verbose_name='دسته بندی‌ها')
    tags = models.ManyToManyField(TagArticle, related_name='portfolio_tags', verbose_name='برچسب‌ها')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # حذف فواصل چپ و راست از نام دسته بندی
        self.title = self.title.strip()
        super().save(*args, **kwargs)
