from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"title": "Home"}
    return render(request, "index.html", context)

def sell(request):
    context = {"title": "Sell"}
    return render(request, "sell.html", context)
    #return HttpResponse("<h1 style='color:white;background-color:blue;'>Sell</h1><a href='./'>Home</a>")

def lend(request):
    context = {"title": "Lend"}
    return render(request, "lend.html", context)
    #return HttpResponse("Lend a book...")
