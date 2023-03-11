"""teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import mainapp.views as mainapp

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', mainapp.main, name="main"),
    path("about/", mainapp.about, name="about"),
    path('blog_single/', mainapp.blog_single, name="blog_single"),
    path('category/', mainapp.category, name="category"),
    path('contact/', mainapp.contact, name="contact"),
    path('homepage_2/', mainapp.homepage_2, name="homepage_2"),
    # path('index/', mainapp.index),
    path('search/', mainapp.search, name="search"),

]


