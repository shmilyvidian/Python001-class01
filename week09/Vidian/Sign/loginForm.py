from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=8, label="用户名", required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': '请输入用户名'
                                   }
                               ))
    password = forms.CharField(min_length=8, label="密码", required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': '请输入密码'
                                   }
                               ))
