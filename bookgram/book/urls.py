from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('home', views.home, name="home"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>',views.delete,name="delete")
]