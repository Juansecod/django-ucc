from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Book

# Create your views here.
def index(request):
    context = {"title": "Home"}
    print(Book.objects.all()[1])
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

# CRUD books
def book_list(request):
    context = {'title': 'Books'}
    """ messages.error(request, "The request it's fine...")
    messages.warning(request, "The request it's fine...")
    messages.success(request, "The request it's fine...") """
    context["books"] = Book.objects.all()
    return render(request, "books/index.html", context)

def create_book(request):
    if(request.method == 'GET'):
        return render(request, "books/create.html", {'title': "Create Book"})
    elif(request.method == 'POST'):
        try:
            book = Book()
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.pages = request.POST.get("pages")
            book.publication_date = request.POST.get("publication_date")
            book.save()
            messages.success(request, "Book created!")
        except:
            messages.error(request, "Something way wrong...")
            
        return redirect("list_books")
        
def delete_book(request, id):
    try:
        book = Book.objects.get(pk = id)
        book.delete()
        messages.success(request, "Book deleted!")
    except:
        messages.error(request, "Something way wrong...")

    return redirect("list_books")

