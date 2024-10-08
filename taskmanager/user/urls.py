from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('register/', views.register_user, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]