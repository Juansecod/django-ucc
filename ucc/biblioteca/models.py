from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
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