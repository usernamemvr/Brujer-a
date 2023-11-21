from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author': 'JK rowling',
        'title': 'Harry potter',
        'content': 'first post content',
        'date_posted': 'August 12, 2023'
    },
    {
        'author': 'William shakesphere',
        'title': 'Merchant of venice',
        'content': 'second post content',
        'date_posted': 'August 12, 1999'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

