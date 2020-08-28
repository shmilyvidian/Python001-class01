from django.shortcuts import render, HttpResponse, redirect, reverse
from .loginForm import LoginForm
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    param = {}
    param['msg'] = '首页'
    return render(request, 'index.html', param)


def error(request, msg):
    print(msg)
    param = {}
    param['msg'] = msg
    return render(request, 'error.html', param)


def login(request):
    if request.method == 'GET':
        loginForm = LoginForm()
        return render(request, 'login.html', {'form': loginForm})
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = auth.authenticate(request,
                                     username=username,
                                     password=password
                                     )
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse('login success', user)
            else:
                isExist = User.objects.filter(username=username).exists()
                if isExist:
                    url = reverse('error', kwargs={'msg': '用户名已存在'})
                    return redirect(url)
                else:
                    User.objects.create_user(
                        username=username,
                        password=password
                    )
                    return HttpResponse('sign success')
        else:
            url = reverse('error', kwargs={'msg': '登录失败，无效参数'})
            return redirect(url)
