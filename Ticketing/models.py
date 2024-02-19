from django.db import models
from MZI.models import Base_Model


class Ticket(Base_Model):
    PRIORITY_CHOICES = [
        ('کم', 'کم'),
        ('متوسط', 'متوسط'),
        ('زیاد', 'زیاد'),
    ]
    USER_TYPE_CHOICES = [
        ('گزینه 1', 'گزینه 1'),
        ('گزینه 2', 'گزینه 2'),
        ('گزینه 3', 'گزینه 3'),
    ]

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='نام و نام خانوادگی')
    subject = models.CharField(max_length=20, blank=True, null=True, verbose_name='موضوع')
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, verbose_name='نوع کاربری')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, verbose_name='درجه اهمیت')
    phone_number = models.CharField(max_length=15, verbose_name='شماره تماس', blank=True, null=True)
    email = models.EmailField(verbose_name='ایمیل', blank=True, null=True)
    additional_description = models.TextField(blank=True, null=True, verbose_name='توضیحات تکمیلی')

    def __str__(self):
        return f'{self.subject} - {self.name}'
