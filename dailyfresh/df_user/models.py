from django.db import models
from db.base_model import BaseModel   #  导入抽象模型基类


# Create your models here.
class PassportManager(models.Manager):
    '''
    用户账户模型管理器类
    '''
    def add_one_passport(self,username,password,email):
        '''
        添加一个用户注册信息
        '''
        models_class = self.model

        # 创建模型类对象
        passport = models_class()
        passport = Passport()
        # 创建了一个 Passport()的对象,名字为 passport
        passport.username = username
        # 对象 passport的参数passport.username 为 POST请求接受的 username
        passport.password = password
        passport.email = email
        # 使用 save()保存到数据库当中
        passport.save()

        # 返回一个passport 对象
        return passport



class Passport(BaseModel):
    '''
    用户账户类
    '''
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField (verbose_name="邮箱")


    # 在类当中创建了一个对象,对象的类方法在上面
    objects = PassportManager()  # 自定义模型管理器对象

    class Meta:
            db_table = "s_user_account"     # 一般不适用默认的表名,所以创建一个自定义表名

