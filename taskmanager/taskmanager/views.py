# from django.http import HttpResponse
from django.shortcuts import render
from tiket.views import tikets_list

# def home_page(request):
#     return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

