import pymysql
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #加入引用
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from apitest.models import Apitest, Apistep, Apis
from django.contrib.auth import authenticate, login

# Create your views here.
def test(request):
    return HttpResponse("hello test") #返回HttpResponse响应函数
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username') #获取Login.HTML的登录名
        password = request.POST.get('password') #获取Login.HTML的密码
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username #session
            response = HttpResponseRedirect('/home/') #登录成功后跳转到首页
            return response
        else:
            return render(request, 'login.html', {'error':'username or password error !'})
    return render(request,'login.html')
def home(request):
    return render(request, 'home.html')
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

# 接口管理
@login_required
def apitest_manage(request):
    username = request.session.get('user', '')
    apitest_list = Apitest.objects.all() #读取所有流程接口参数
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})

# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = Apistep.objects.all() #读取所有流程接口步骤
    return render(request, 'apistep_manage.html', {'user': username, 'apisteps': apistep_list})

# 单一接口管理
@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    return render(request, 'apis_manage.html', {'user': username, 'apiss': apis_list})

# 测试报告
@login_required
def test_reprort(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()
    db = pymysql.Connect(user='root', db='autotest', passwd='', host='127.0.0.1')
    cursor = db.cursor()
    sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request, "report.html", {'user':username,
                                           'apiss':apis_list,
                                           'apiscounts':apis_count,
                                           'apis_pass_counts':apis_pass_count,
                                           'apis_fail_counts':apis_fail_count})