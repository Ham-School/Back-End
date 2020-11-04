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
<<<<<<< HEAD
    return render(request, "vistas/cursos/colores.html")

def finalK (request):
    return render(request, "vistas/cursos/final.html")

def primaria (request):
    return render(request, "vistas/cursos/pplprm.html")

def Alfabeto (request):
    return render(request, "vistas/cursos/alfabetoprim.html")

def Números (request):
    return render(request, "vistas/cursos/numerosprim.html")

def Colores (request):
    return render(request, "vistas/cursos/coloresprim.html")

def Figuras (request):
    return render(request, "vistas/cursos/fgeoprim.html")    

def cuerpo (request):
    return render(request, "vistas/cursos/partescuerpoprim.html")

def Pronombres (request):
    return render(request, "vistas/cursos/pronomprim.html")  
=======
    return render(request, "vistas/cursos/colores.html")
>>>>>>> a270ec05881fec014219ca3a086c6790dd4738a7
