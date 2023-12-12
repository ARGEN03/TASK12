from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=55)
    nick_name = models.CharField(max_length=85, blank=True)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return f'{self.name} {self.nick_name    }'