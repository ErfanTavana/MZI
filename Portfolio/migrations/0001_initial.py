# Generated by Django 5.0.1 on 2024-03-04 14:42

import MZI.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0003_alter_categoryarticle_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.CharField(default=MZI.models.generate_complex_id, editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='شناسه')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='تاریخ حذف')),
                ('is_ok', models.BooleanField(default=True, verbose_name='آیا تایید شده است؟')),
                ('is_changeable', models.BooleanField(default=True, verbose_name='قابل تغییر است؟')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان نمونه کار')),
                ('description', models.TextField(verbose_name='توضیحات نمونه کار')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio_images/', verbose_name='عکس نمونه کار')),
                ('categories', models.ManyToManyField(related_name='portfolio_categories', to='Article.categoryarticle', verbose_name='دسته بندی\u200cها')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_by_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='portfolio_tags', to='Article.tagarticle', verbose_name='برچسب\u200cها')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
