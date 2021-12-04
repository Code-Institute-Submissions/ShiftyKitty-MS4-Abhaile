from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='all_subscriptions'),
    path('subscribe/', views.subscribe, name='subscribe'),
    
]