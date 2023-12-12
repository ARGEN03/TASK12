from django.db import models
from author.models import Author

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=80)
    created_at = models.DateField(null=True)


    def __str__(self) -> str:
        return f'{self.title}'