from django.conf.urls import url
from df_user import views


urlpatterns = [

    #url(r'index/',views.register),
    url(r'^register/$',views.register), # 用于返回给用户注册页 and用户注册提交表单信息
]