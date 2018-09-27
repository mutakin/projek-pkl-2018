from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'ascobar/index.html',{})


def paket(request):
	return render(request,'ascobar/paket.html',{})

def faq(request):
	return render(request,'ascobar/faq.html',{})


def projects(request):
	return render(request,'ascobar/projects.html')

def listrik_sopan(request):
	return render(request,'ascobar/listrik_sopan.html')

def kontak(request):
	return render(request,'ascobar/kontak.html')


	