from tabnanny import verbose
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호')
    #user_name = models.CharField(max_length=16, unique=True, verbose_name='유저 이름')

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'

# Create your models here.
