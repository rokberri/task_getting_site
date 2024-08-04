from django.shortcuts import render
from .models import Tiket

def tikets_list(request):
    tikets = Tiket.objects.all().order_by('-date')
    return render(request, 'tikets/tiket_list.html', {'tikets': tikets})

# def tiket_page(request, slug):
#     tikets = Tiket.objects.get(slug=slug)
#     return render(request, 'tikets/tiket_page.html', {'tikets': tikets})