from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,widget=forms.TextInput(attrs={'class': 'form-control', 'value':'visitor'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'value':'aa123123'}))