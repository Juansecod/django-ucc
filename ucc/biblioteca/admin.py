from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "pages", "publication_date", "classification"]
    search_fields =["title", "author"]
    list_filter = ["classification", "publication_date"]

admin.site.register(Book, BookAdmin)
