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
    path("books/edit/<int:id>",  views.index, name="edit_book"),
    path("books/delete/<int:id>",  views.delete_book, name="delete_book"),
]