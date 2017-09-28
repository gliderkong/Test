from django.shortcuts import render
from django .template import loader

# Create your views here.
# http: //127.0.0.1:8000 /user/register/

def register(request):
    '''
    显示注册页面
    '''
    return render (request, 'df_user/register.html')