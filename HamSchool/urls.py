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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from HamSchool.Apps.vistas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pplkinder.html', views.kinder),
    path('index.html', views.index),
    path('numeros.html', views.numk),
    path('abc.html', views.abck),
    path('losanimales.html', views.animk),
    path('colores.html', views.coloresk),
    path('final.html', views.finalK),
    path('pplprm.html', views.primaria),
    path('alfabetoprim.html', views.Alfabeto),
    path('numerosprim.html', views.Números),
    path('coloresprim.html', views.Colores),
    path('fgeoprim.html', views.Figuras),
    path('partescuerpoprim.html', views.cuerpo),
    path('pronomprim.html', views.Pronombres),
    path('finalprim.html', views.finalp),
    path('pplsec.html', views.secundaria),

    path('logout/', views.logout_requesr, name="logout"),
    path('', views.login_request, name="login"),
    path('login', views.login_request, name="login"),
    path('register', views.register_request, name="register")

    
]

urlpatterns += staticfiles_urlpatterns()