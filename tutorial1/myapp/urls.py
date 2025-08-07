from django.contrib import admin
from django.urls import path
from myapp import views  # Import views from myapp

urlpatterns = [
    path('func/', views.func),
    path('list_view/', views.list_view),
    path('getval/<str:a>/<str:b>/', views.getval),
]
