from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>You are at Blog-home</h1>')

def about(request):
    return HttpResponse('<h1>You are at Blog-about</h1>')
