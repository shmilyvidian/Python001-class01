from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'login/', views.login),
    path('error/<msg>/', views.error, name='error'),
]
