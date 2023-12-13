
1. **Создайте Django-проект:**
   
   В вашем терминале выполните следующие команды:

   ```bash
   django-admin startproject config
   cd config
   ```

2. **Создайте приложения `author` и `book`:**
   
   ```bash
   python3 manage.py startapp author
   python3 manage.py startapp book
   ```

3. **Определите модель автора (`author/models.py`):**

   ```python
   # author/models.py
   from django.db import models

   class Author(models.Model):
    name = models.CharField(max_length=55)
    nick_name = models.CharField(max_length=85, blank=True)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return f'{self.name} {self.nick_name}'


   ```

4. **Определите модель книги (`book/models.py`):**

   ```python
   # book/models.py
   from django.db import models
   from author.models import Author

    class Book(models.Model):

        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
        genre = models.CharField(max_length=80)
        created_at = models.DateField(null=True)


    def __str__(self) -> str:
        return f'{self.title}'
   ```

5. **Настройте приложения в `settings.py`:**

   В файле `myproject/settings.py` добавьте в раздел `INSTALLED_APPS` ваши приложения:

   ```python
   INSTALLED_APPS = [
       # ...
       'author',
       'book',
   ]
   ```

6. **Выполните миграции:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **CRUD в файлах заметок (`readme.md`):**

   - **Create (Создание):**
     - Создание автора: `Author.objects.create(name='Имя', date_of_birth ='1990-01-01', nick_name='Псевдоним')`
     - Создание книги: 
       ```python
       author = Author.objects.get(name='Имя')
       Book.objects.create(title='Название книги', date_of_birth='2022-01-01', genre='Жанр', author=author)
       ```

   - **Read (Чтение):**
     - Получение всех авторов: `Author.objects.all()`
     - Получение всех книг: `Book.objects.all()`
     - Получение книги по названию: `Book.objects.get(title='Название книги')`

   - **Update (Обновление):**
     - Обновление автора: 
       ```python
       author = Author.objects.get(name='Имя')
       author.nick_name = 'Новый псевдоним'
       author.save()
       ```
     - Обновление книги:
       ```python
       book = Book.objects.get(title='Название книги')
       book.genre = 'Новый жанр'
       book.save()
       ```

   - **Delete (Удаление):**
     - Удаление автора: `Author.objects.get(name='Имя').delete()`
     - Удаление книги: `Book.objects.get(title='Название книги').delete()`
