from django.shortcuts import render,redirect
from django .template import loader
from df_user.models import Passport

# Create your views here.
# http: //127.0.0.1:8000 /user/register/

def register(request):
    '''
    显示注册页面
    '''
    return render (request, 'df_user/register.html')


#----------------------------------------------------------------
# 用户在注册页面中 提交表单信息之后,发送到当前的视图函数中
# 创建一个视图函数,用于接受用户的注册信息

def register_handle(request):
    '''
    用户注册处理
    '''
    # 1 接受用户提交的信息
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 2 讲用户的注册信息保存到数据库
    passport = Passport()
    # 创建了一个 Passport()的对象,名字为 passport
    passport.username = username
    # 对象 passport的参数passport.username 为 POST请求接受的 username
    passport.password = passport
    # 同理
    passport.email = email
    # 同理
    passport.save()


    # 3 跳转到登陆页面
    return redirect('/')


