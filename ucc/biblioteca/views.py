from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Book, Booking

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
    context["books"] = Book.objects.all()
    return render(request, "books/index.html", context)

def create_book(request):
    if(request.method == 'GET'):
        return render(request, "books/form.html", {'title': "Create Book"})
    elif(request.method == 'POST'):
        try:
            book = Book()
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.pages = request.POST.get("pages")
            book.publication_date = request.POST.get("publication_date")
            book.save()
            messages.success(request, "Book created!")
        except Exception as e:
            print(e)
            messages.error(request, "Something way wrong...")
  
        return redirect("list_books")

def edit_book(request, id):
    if request.method == "POST":
        try:
            book = Book.objects.get(pk = id)
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.pages = request.POST.get("pages")
            book.publication_date = request.POST.get("publication_date")
            book.save()
            messages.success(request, "Book created!")
        except Exception as e:
            print(e)
            messages.error(request, "Something way wrong...")
        return redirect('list_books')
    else:
        book = Book.objects.get(pk = id)
        context = {"book": book, "title": "Edit book"}
        return render(request, "books/form.html", context)

def delete_book(request, id):
    try:
        book = Book.objects.get(pk = id)
        book.delete()
        messages.success(request, "Book deleted!")
    except Exception as e:
        print(e)
        messages.error(request, "Something way wrong...")

    return redirect("list_books")

# CRUD bookings
def booking_list(request):
    context = {'title': 'Bookings'}
    context["bookings"] = Booking.objects.all()
    return render(request, "bookings/index.html", context)

def create_booking(request):
    if(request.method == 'GET'):
        context = {'title': "Create Booking"}
        context['books'] = Book.objects.all()
        return render(request, "bookings/form.html", context)
    elif(request.method == 'POST'):
        print(request.POST)
        username = request.POST.get("username")
        book_id = request.POST.get("book")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        try:
            book = Book.objects.get(pk = book_id)
            booking = Booking(
                username = username, 
                book = book, 
                start_date = start_date, 
                end_date = end_date
            )
            booking.save()
            messages.success(request, "Booking created!")
        except Exception as e:
            print(e)
            messages.error(request, "Something way wrong...")
  
        return redirect("list_bookings")

def edit_booking(request, id):
    if request.method == "POST":
        try:
            book = Booking.objects.get(pk = id)
            book.username = request.POST.get("username")
            book.end_date = request.POST.get("end_date")
            book.save()
            messages.success(request, "Booking updated!")
        except Exception as e:
            print(e)
            messages.error(request, "Something way wrong...")
        return redirect('list_bookings')
    else:
        booking = Booking.objects.get(pk = id)
        books = Book.objects.all()
        context = {"booking": booking, "books": books, "title": "Edit booking"}
        return render(request, "bookings/form.html", context)

def delete_booking(request, id):
    try:
        booking = Booking.objects.get(pk = id)
        booking.delete()
        messages.success(request, "Booking deleted!")
    except Exception as e:
        print(e)
        messages.error(request, "Something way wrong...")

    return redirect("list_bookings")
