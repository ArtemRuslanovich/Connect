"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('about_us.html', views.about_us, name='about_us.html'),  # Добавьте эту строку
    path('blog.html', views.blog, name='blog.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('gallery.html', views.gallery, name='gallery.html'),
    path('main.html', views.main, name='main.html'),
    path('schedule.html', views.schedule, name='schedule.html'),
    path('blog-single.html', views.blog_single, name='schedule.html')
]
