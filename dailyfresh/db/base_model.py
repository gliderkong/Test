from django.db import models


class BaseModel(models.Model):
    '''
    模型类 抽象基类
    '''
    credits_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False , verbose_name="去除")

    class Meta:
        abstract = True # db不是一个应用,所以把不能注册,需要说明是一个抽象类

