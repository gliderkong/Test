from django.conf.urls import url
from df_user import views


urlpatterns = [

    url(r'index/',views.register), # 用于返回给用户注册页面
    url(r'^register_handle',views.register_handle), # 用户注册提交表单信息
]