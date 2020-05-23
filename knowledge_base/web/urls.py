from django.urls import path, include
from . import views
from haystack.views import SearchView

app_name = 'web'
urlpatterns = [
    path('', views.index),
    path('search_form/', views.search_form),
    path('search1/', views.search1),
    path('index/', views.index),
    path('bingji/', views.bingji),
    path('zhifa/', views.zhifa),
    path('fangji/', views.fangji),
    path('jiegou/', views.jiegou),
    path('shiyong/', views.shiyong),
    path('jieguo/', views.jieguo),
    path('about/', views.about),
    path('contact/', views.contact),
    path('bingjixibie/', views.bingjixibie),
    path('zhibingjili/', views.zhibingjili),
    path('bingzheng/', views.bingzheng),
    path('lifang/', views.lifang),
    path('feixi/', views.feixi),
    path('xinxi/', views.xinxi),
    path('piwei/', views.piwei),
    path('liangzang/', views.liangzang),
    path('shenxi/', views.shenxi),
    path('gandan/', views.gandan),
    path('zhishiku/', views.zhishiku),
    path('web/', views.web),
    path('search/', include('haystack.urls')),
]
