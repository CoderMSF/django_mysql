#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$', views.index_view),
    url(r'^show/$', views.show_view)
]


