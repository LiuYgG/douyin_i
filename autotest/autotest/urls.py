"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apitest import views # 流程接口测试模块
from product import views as proviews #产品模块
from bug import views as bugsviews
from set import views as setViews
from apptest import views as appcaseViews
from webtest import views as webcaseViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test), #加入关键路径及函数
    path('login/', views.login), #加入登录路径及函数
    path('home/', views.home), #加入主页路径及函数
    path('logout/', views.logout), #加入退出路径及函数
    path('report/', views.test_reprort),
    path('product_manage/', proviews.product_manage),
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage),
    path('apis_manage/', views.apis_manage),
    path('bug_manage/', bugsviews.bug_manage),
    path('set_manage/', setViews.set_manage),
    path('user_manage/', setViews.set_user),
    path('appcase_manage/', appcaseViews.appcase_manage),
    path('appcasestep_manage/', appcaseViews.appcasestep_manage),
    path('webcase_manage/', webcaseViews.webcase_manage),
    path('webcasestep_manage/', webcaseViews.webcasestep_manage),
]
