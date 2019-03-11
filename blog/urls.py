# coding=utf-8
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import  views
from  django.conf  import settings


urlpatterns = [
   url(r'^index/$',views.index),
   url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
   url(r'^editor/(?P<article_id>[0-9]+)$',views.editor_page,name='editor_page'),

   url(r'^edit_article/$', views.add_article,name="add_article"),

   url(r'^edit_article/action$', views.edit_action,name='edit_action'),

   url(r'^login/$', views.login,name="login"),

   url(r'^login/logins/$', views.logins,name="logins"),

   url(r'^register/$', views.register,name="register"),

   url(r'^register_user_info$', views.register_user_info,name="register_user_info"),

   url(r'^add_article/(?P<article_id>[0-9]+)$', views.editor_page,name="add_article"),

   url(r'^login_ajax/$', views.login_ajax,name="login_ajax"),
   url(r'^user_main/$', views.user_main,name="user_main"),
   url(r'^ajax_register_info/$', views.ajax_register_info,name="ajax_register_info"),
]