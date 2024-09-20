from django.contrib import admin
from .models import Book, Booking

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "pages", "publication_date", "classification"]
    search_fields =["title", "author"]
    list_filter = ["classification", "publication_date"]

admin.site.register(Book, BookAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "book", "start_date", "end_date"]
    search_fields =["username", "book"]
    list_filter = ["start_date", "end_date"]

admin.site.register(Booking, BookingAdmin)
