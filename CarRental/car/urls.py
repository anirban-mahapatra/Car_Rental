from django.contrib import admin
from django.urls import include, path
from car import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login),
    path('register/',views.register),
    path('about/',views.about),
    path('contact/',views.contact)
]
