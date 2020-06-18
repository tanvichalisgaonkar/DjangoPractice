from django.shortcuts import render
from . import form
# Create your views here.

def index(request):
	return render(request,'formapp/index.html')


def form_name_view(request):
	forms = form.FormName() 

	if request.method == 'POST':
		forms = form.FormName(request.POST)

		if forms.is_valid():
			print("Validation Success")
			print("Name: " +forms.cleaned_data['name'])
			print("Mail: " +forms.cleaned_data['email'])
			print("Text: " +forms.cleaned_data['text'])


	return render(request,'formapp/form_page.html',{'form':forms})