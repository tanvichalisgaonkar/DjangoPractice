from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import UserInfo
# Create your views here.
def home(request):
	dict_show = {'welcome_msg':'Welcome!',
	'info_msg':'Go to /user to see the list of user information!'
	}
	return render(request,'home.html',context = dict_show)


def help(request):
	dict_one ={'help_msg' : 'This is a Help Support Page.'}
	return render(request,'help.html',context = dict_one)

def user(request):
	usr_list = UserInfo.objects.order_by('first_name')
	dict_user = {'user_info' : 'Welcome to user info page',
	'user_detail' : usr_list}
	return render(request,'user.html',context = dict_user)
