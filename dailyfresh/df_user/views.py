from django.shortcuts import render,redirect


from django.views.decorators.http import require_POST,require_GET,require_http_methods
from django .template import loader
from df_user.models import Passport



#----------------------------------------------------------------
# 在注册页面中表单请求方式进行限定,创建一个装饰器,在不影响函数的情况下添加新的功能
# 原生 限制非法请求通道装饰器方法
'''
def request_POST (view_func):
    def wrapper(request,*args,**kwargs):
        if request.method != 'POST':
            # 如果不是post请求则拒绝提交,同时返回一个提示信息
            return HttpResponseNotAllowed('not allowed')
        else :
            return view_func(request, *args, **kwargs)
    return  wrapper
'''

# Create your views here.
# http: //127.0.0.1:8000 /user/register/

# Django 封装的装饰器方法
@require_http_methods(['GET','POST'])

def register(request):
    '''
    显示注册页面 / 用户注册登陆合二为一  添加到一个 视图函数当中
    '''
    # 视图函数只负责接受发送来的请求,无论是什么方式提交,只要符合即会返回指定页面
    # 通过网址登陆网页,全部向服务器发送 get 请求, 所以可以 设置为 get 参数
    # 注册表单向服务器发送为post请求方式,所以可以设置为 只有POST请求方式才可以跳转

    if request.method == 'GET':
        return render (request,'df_user/register.html')

    elif request.method == "POST":
        '''
        用户注册处理

        '''
        # 用户在注册页面中 提交表单信息之后,发送到当前的视图函数中
        # 创建一个视图函数,用于接受用户的注册信息

        # 1 接受用户提交的信息
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')

        # 2 将用户的注册信息保存到数据库


        # 3 跳转到登陆页面
        return redirect('/')

        # return "OK"







