from django.urls import path
from . import views

app_name = 'tiket'

urlpatterns = [
    path('tiket_list/', views.tikets_list, name='list'),
    path('add_ticket/', views.add_ticket, name='create_ticket'),
    path('test_page/', views.test_func, name='test'),
    path('update/<int:ticket_id>/', views.update, name='update'),
]