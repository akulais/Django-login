from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from django.http import HttpResponse
from .forms import User_form, Auth_form
from django.views.generic.base import TemplateView
from django.views.generic import View

class User(object):
	template=''
	context = None
	user = None
	def get_template(self):
		if self.template == '':
			raise ImproperlyConfigured('Not available')
		return self.template

class Index(TemplateView):
	template = 'accounts/login.html'
	def get(self,request):
		form = {'form': Auth_form}
		return render(request, self.template, form)

class Login(View):
	form = Auth_form
	def get(self, request):
		context = {'form':self.form()}
		return render(request, 'accounts/login.html', context)
	def post(self, request):
		print 'here'
		form = self.form(data=request.POST)
		print form
		print 'here'
		print 'here2'
		print 'here3'
		print form.errors
		if form.is_valid():
			print 'here4'
			username = form.cleaned_data['username']
			print 'here5'
			password = form.cleaned_data['password']
			print 'here6'
			user = authenticate(username=username, password=password)
			print user
			print 'here7'
			if user is not None:
				print 'here8'
				login(request, user)
				print 'here9'
				return render(request, 'accounts/success.html')
			else:
				print 'here10'
				context = {'form':form}
				return render(request, 'accounts/login.html', context)
		else:
			print 'here11'
			return redirect('/')

class Register(TemplateView):
	form = User_form
	def get(self, request):
		context = {'form': self.form()}
		return render(request, 'accounts/register.html', context)
	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'accounts/success.html')
		else:
			context = {'form':form}
			return render(request, 'accounts/register.html', context)

class Success(TemplateView):
	template = 'accounts/success.html'
	def get(self,request):
		return render(request, self.template)

# class Logout(View):
def logout(request):
	print 'loggin out'
	logout(request)
	return render(request, 'accounts/login.html')