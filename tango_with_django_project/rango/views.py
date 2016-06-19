from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = "Rango says hey there world!"
    content += '<br /><a href="about/">About</a>'
    return HttpResponse(content)

def about(request):
    content = "Rango says hey, this is the About page"
    content += '<br /><a href="/rango/">Index</a>'
    return HttpResponse(content)