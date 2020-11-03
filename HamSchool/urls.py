"""HamSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from HamSchool.Apps.vistas import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('article.html/', views.article),
    path('article.html/index.html', views.index),
    path('article.html/article.html', views.article),
    path('pplkinder.html', views.kinder),
    path('index.html', views.index),
    path('numeros.html', views.numk),
    path('abc.html', views.abck),
    path('losanimales.html', views.animk),
    path('colores.html', views.coloresk),
   
]

urlpatterns += staticfiles_urlpatterns()