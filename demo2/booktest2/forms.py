from django import forms
from .models import *

class LoginForms(forms.Form):
    username = forms.CharField(label="用户名", max_length=20, required=True, widget=forms.TextInput(attrs={"id":"name", "class":"form-control", "placeholder":"输入用户名"}))
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={"class":"form-control", "id":"password", "placeholder":"输入密码"}))


class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="重复密码", required=True, widget=forms.PasswordInput(attrs={"class":"form-control", "id":"registpassword2", "placeholder":"输入确认密码"}))
    class Meta:
        model = BookUser
        fields = ["username", "password", "telephone"]
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername", "placeholder":"输入用户名"}),
            "password": forms.TextInput(attrs={"id": "registpassword", "placeholder": "输入密码"}),
            "telephone": forms.TextInput(attrs={"id": "registtelephone", "placeholder": "输入手机号"}),

        }