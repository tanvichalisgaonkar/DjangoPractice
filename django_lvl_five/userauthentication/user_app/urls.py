from django.urls import path,re_path 
from user_app import views

app_name = 'user_app'

urlpatterns =[
re_path(r'^register/$',views.register,name = 'register'),
re_path(r'^user_login/$',views.user_login,name='user_login')
]