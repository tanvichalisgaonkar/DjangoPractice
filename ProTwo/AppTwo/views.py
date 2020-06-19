from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import UserInfo
from . import forms

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
	form = forms.SignUpForm()

	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)

		if form.is_valid():
			print("Validation Success")
			print("First Name: " +form.cleaned_data['first_name'])
			print("Last Name: "  +form.cleaned_data['last_name'])
			print("Mail: " +form.cleaned_data['email'])
			new_user = form.save(commit = True)
			return home(request)
		else:
			print("Invalid Form")

	return render(request,"user.html",{'form':form})

	
