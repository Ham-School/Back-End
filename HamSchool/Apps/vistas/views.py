from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def register (request):
    return render(request, "vistas/login/register.html")    

def index (request):
    return render(request, "vistas/index.html")

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

def finalp (request):
    return render(request, "vistas/cursos/finalprim.html")


def secundaria (request):
    return render(request, "vistas/cursos/pplsec.html")


def logout_requesr(request):
    logout(request)
    messages.info(request, "salida exitosa")
    return redirect("vistas/index.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contaseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contaseña)

            if user is not None:
                login(request, user)
                return redirect("index.html")
            else:
                messages.error(request, "Usuario o Contraseña invalidad")
                
    form = AuthenticationForm()
    return render(request, "vistas/login/login.html")