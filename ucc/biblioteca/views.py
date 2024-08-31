from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    context = {"title": "Home"}
    print(Book.objects.all()[0])
    return render(request, "index.html", context)

def sell(request):
    context = {"title": "Sell"}
    return render(request, "sell.html", context)
    #return HttpResponse("<h1 style='color:white;background-color:blue;'>Sell</h1><a href='./'>Home</a>")

def lend(request):
    context = {"title": "Lend"}
    return render(request, "lend.html", context)
    #return HttpResponse("Lend a book...")
    
def calculator(request):
    context = {"title": "calculator"}
    if request.method == "GET":
        return render(request, "form.html", context)
    elif request.method == "POST":
        n1 = int(request.POST.get("n1"))
        n2 = int(request.POST.get("n2"))
        context["result"] = n1 + n2
        return render(request,"form.html",context)

def sum(request, n1, n2):
    return render(request, "form.html", {"title":"sum", "result":n1+n2})