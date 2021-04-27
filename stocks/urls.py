from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.stockDetails, name="stock-details"),
    path('today_data', views.todayData, name="today-data")
]
