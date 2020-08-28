from django import forms
from django.contrib import auth
from .models import User


class CheckLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=12,
        min_length=6,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '用户名长度不能超过12',
            'min_length': '用户名长度不能小于6',
        })
    password = forms.CharField(
        required=True,
        max_length=12,
        min_length=8,
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码长度不能超过12',
            'min_length': '密码长度不能小于8',
        })


    def clean(self):
        try:
            User.objects.get(username=self.clean_data.get('username'))
            isExist = User.objects.filter(name='admin', password='admin').count()
        except:
            #{'username':'用户名不存在'} 里面的username就是你的用户输入的那个input的提示信息
            raise ValidationError({'username':'用户名不存在'})
        user=auth.authenticate(username=self.clean_data.get('username'),
                           password=self.clean_data.get('password')) 
        if not user:
            raise ValidationError({'password':'密码错误'})
        
        self.clean_data['user']=user
        return self.clean_data # self.clean_data 验证成功返回的验证数据
