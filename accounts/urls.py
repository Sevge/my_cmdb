from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'login/$', views.Login.as_view(), name='login'),
    url(r'logout/$', views.logout, name='logout'),
]