from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido a la biblioteca")

def view_blue(request):
    return HttpResponse("<h1 style='color:white;background-color:blue;'>Esto esta en un fondo azul</h1>")
