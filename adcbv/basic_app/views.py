from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Function Based View
# def index(request):
# 	return render(request,'index.html')

# Class Based Views
# class CBView(View):
# 	def get(self,request):
# 		return HttpResponse("Class Base views are cool!")

class IndexView(TemplateView):
	template_name = 'index.html'
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['insert'] = 'Basic insert'
		return context