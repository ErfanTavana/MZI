from django.db import models
from django.contrib.auth.models import User
from  MZI.models import Base_Model
class AdminMZI(Base_Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='ادمین')
    is_admin = models.BooleanField(default=False)