from django.shortcuts import render, HttpResponse, redirect
from .models import Tiket
from .forms import TicketFrom

def tikets_list(request):
    tikets = Tiket.objects.all().order_by('-date')
    return render(request, 'tiket/tiket_list.html', {'tikets': tikets})

def add_ticket(request):
    if request.method == "POST":
        # new_ticket = Tiket(owner=request.POST.get("owner"),body=request.POST.get("body"),)
        Tiket.objects.create(owner=request.POST.get("owner"),body=request.POST.get("body"),)
        return redirect("tiket:list")
    else:
        return render(request, 'tiket/create_ticket.html',{'ticketform':TicketFrom(request)})
        # return redirect("tiket:list")
    # return render(request, 'tiket/tiket_list.html')
    # if request.method == "POST":
    #     new_ticket = TicketFrom(request.POST)
    #     if new_ticket.is_valid():
    #         print(request.POST)
    #         add_ticket(request, new_ticket.save())
    #     return redirect("tiket:list")
    # else:
    #      new_ticket = TicketFrom()

# def tiket_page(request, slug):
#     tikets = Tiket.objects.get(slug=slug)
#     return render(request, 'tikets/tiket_page.html', {'tikets': tikets})
def test_func(request):

    if request.user.is_authenticated:
        return HttpResponse('authenticated')
    else: 
        return HttpResponse('not authenticated')
    
def update(request, ticket_id):
    ticket =Tiket.objects.get(id=ticket_id)
    ticket.status = not ticket.status
    ticket.save()
    return redirect("tiket:list")