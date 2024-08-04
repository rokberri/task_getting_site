# from django.http import HttpResponse
from django.shortcuts import render
from tiket.views import tikets_list

def hame_page(request):
    return tikets_list(request)

def about(request):
    return render(request, 'about.html')

