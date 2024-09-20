from django.urls import path
from . import views

urlpatterns = [
    path("",  views.index, name="index"),
    path("sell", views.sell, name="sell"),
    path("lend", views.lend, name="lend"),
    path("sum/<int:n1>/<int:n2>", views.sum, name="sum"),
    path("calculator", views.calculator, name="calculator"),
    
    # CRUD books
    path("books",  views.book_list, name="list_books"),
    path("books/create",  views.create_book, name="create_book"),
    path("books/edit/<int:id>",  views.edit_book, name="edit_book"),
    path("books/delete/<int:id>",  views.delete_book, name="delete_book"),
    
    # CRUD bookings
    path("bookings",  views.booking_list, name="list_bookings"),
    path("bookings/create",  views.create_booking, name="create_booking"),
    path("bookings/edit/<int:id>",  views.edit_booking, name="edit_booking"),
    path("bookings/delete/<int:id>",  views.delete_booking, name="delete_booking"),
]