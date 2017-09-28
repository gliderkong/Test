from django.db import models
from db.base_model import BaseModel   #  导入抽象模型基类


# Create your models here.

class Passport(BaseModel):
    '''
    用户账户类
    '''
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField (verbose_name="邮箱")

    class Meta:
            db_table = "s_user_account"     # 一般不适用默认的表名,所以创建一个自定义表名

