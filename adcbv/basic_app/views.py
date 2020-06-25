from django.shortcuts import render
from django.views.generic import (View,TemplateView,
					ListView,DetailView,
					CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models

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

#List View
class SchoolListView(ListView):
	context_object_name = 'schools'
	model = models.School


# Detail View
class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = models.School
	template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
	fields = ('name','principal','location')
	model = models.School
