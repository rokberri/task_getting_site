from django.urls import path
from . import views

app_name = 'tiket'

urlpatterns = [
    path('', views.tikets_list, name='list'),

]