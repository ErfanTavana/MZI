# Generated by Django 5.0.1 on 2024-02-19 06:04

import MZI.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default=MZI.models.generate_complex_id, editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='شناسه')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='تاریخ حذف')),
                ('is_ok', models.BooleanField(default=True, verbose_name='آیا تایید شده است؟')),
                ('is_changeable', models.BooleanField(default=True, verbose_name='قابل تغییر است؟')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='نام دسته بندی')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_by_%(class)s_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.CharField(default=MZI.models.generate_complex_id, editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='شناسه')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='تاریخ حذف')),
                ('is_ok', models.BooleanField(default=True, verbose_name='آیا تایید شده است؟')),
                ('is_changeable', models.BooleanField(default=True, verbose_name='قابل تغییر است؟')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='نام برچسب')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_by_%(class)s_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.CharField(default=MZI.models.generate_complex_id, editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='شناسه')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین به\u200cروزرسانی')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='تاریخ حذف')),
                ('is_ok', models.BooleanField(default=True, verbose_name='آیا تایید شده است؟')),
                ('is_changeable', models.BooleanField(default=True, verbose_name='قابل تغییر است؟')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان مقاله')),
                ('description', models.TextField(verbose_name='توضیحات مقاله')),
                ('image', models.ImageField(blank=True, null=True, upload_to='article_images/', verbose_name='عکس مقاله')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted_by_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='articles', to='Article.category', verbose_name='دسته بندی\u200cها')),
                ('tags', models.ManyToManyField(related_name='articles', to='Article.tag', verbose_name='برچسب\u200cها')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
