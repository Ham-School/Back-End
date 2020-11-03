from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "vistas/index.html")

def login (request):
    return render(request, "vistas/login/index.html")

def article (request):
    return render(request, "vistas/article.html")

def kinder (request):
    return render(request, "vistas/cursos/pplkinder.html")

def numk (request):
    return render(request, "vistas/cursos/numeros.html")

def abck (request):
    return render(request, "vistas/cursos/abc.html")  

def animk (request):
    return render(request, "vistas/cursos/losanimales.html")

def coloresk (request):
    return render(request, "vistas/cursos/colores.html")