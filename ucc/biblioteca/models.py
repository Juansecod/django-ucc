from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False, unique=True)
    author = models.CharField(max_length=100, default="Anonymous")
    pages = models.IntegerField()
    publication_date = models.DateField(help_text="Publication Date")
    CLASSIFICATION_AVAILABLES = (
        (0,""),
        (1,"Romance"),
        (2,"Adventure"),
        (3,"Sci-fi"),
    )
    classification = models.IntegerField(choices=CLASSIFICATION_AVAILABLES, default=0)

    def __str__(self) -> str:
        return f"Title: {self.title}\nAuthor: {self.author}"

class Booking(models.Model):
    username = models.CharField(max_length=100, help_text="Username of user what is booking")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="Book Booked")
    start_date = models.DateField(help_text="Start date of booking")
    end_date = models.DateField(help_text="End date of booking")
    
    def __str__(self) -> str:
        return f"{self.book.title} is booked by {self.username} from {self.start_date} to {self.end_date}"

class User(models.Model):
    email = models.EmailField(max_length = 254, unique = True)
    full_name = models.CharField(max_length = 254)
    password = models.CharField(max_length = 254)
    ROLES = (
        ('A', 'Admin'),
        ('L', 'Librarian'),
        ('S', 'Student')
    )
    rol = models.CharField(max_length=1, choices=ROLES, default='E')