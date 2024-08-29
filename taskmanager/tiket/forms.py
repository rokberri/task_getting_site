from django import forms
from .models import Tiket
 
class TicketFrom(forms.Form):
    owner = forms.CharField()
    body = forms.CharField()
    status = forms.BooleanField().hidden_widget()

    # def save():
    #     ticket