
from django.contrib import admin
from django.urls import path
from pk_portfolio import views
urlpatterns = [
    path('', views.home,name='home'),
]