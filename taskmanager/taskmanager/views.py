# from django.http import HttpResponse
from django.shortcuts import render

def hame_page(request):
    # return HttpResponse('Hello Word!')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About page')
    return render(request, 'about.html')

