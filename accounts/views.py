from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import View
from . import forms


# Create your views here.
def logout(request):
    request.session.flush()
    return redirect(reverse('accounts:login'))

class Login(View):
    def get(self, request):
        login_form = forms.UserForm(request.POST)
        request.session['next'] = request.GET.get('next', reverse('index'))
        if request.session.get('is_login', None):
            return redirect(request.session['next'])
        return render(request, 'accounts/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = forms.UserForm(request.POST)
        msg = '请输入用户名和密码！'
        if login_form.is_valid():
            print(login_form)
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    request.session['is_login'] = True
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    msg = '用户名或密码不正确！'
            except:
                msg = '请检查输入是否正确！'
        return render(request, 'accounts/login.html', {'msg': msg, 'login_form': login_form})