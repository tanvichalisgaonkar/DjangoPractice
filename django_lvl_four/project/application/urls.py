from django.urls import path,re_path
from application import views


#TEmplate Tagging

app_name = 'application'

urlpatterns = [
	re_path(r'^relative/$', views.relative, name = 'relative'),
	re_path(r'^other/$',views.other,name = 'other'), 
]