from django.shortcuts import render

# Create your views here.

def index(request):
	con_dict = {'text': 'hello World','number':100 }
	return render(request,'application/index.html',context = con_dict)

def other(request):
	return render(request,'application/other.html')

def relative(request):
	return render(request,'application/relative_url_template.html')