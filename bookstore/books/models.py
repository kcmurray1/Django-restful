from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    # types choices is used like an ENUM
    TYPES_CHOICES = (
        (0, "Paperback"),
        (1, "Hardcover"),
        (2, "Kindle")
    )
    title = models.CharField(max_length=100)
    price= models.FloatField()
    description = models.CharField(max_length=1000, blank=True)
    book_type = models.IntegerField(choices=TYPES_CHOICES, default=0)

    def __str__(self):
        return f'{self.id}: {self.title} (${self.price}) - ${self.book_type} {self.get_book_type_display()}'
    

class Comment(models.Model):
    content = models.CharField(max_length=250)
    author = models.CharField(max_length=100, blank=True)

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return f"{self.content} by {self.author} for {self.book}"


# Rating (user can rate a book anyonymously)
"""
model (1,2,3,4,5)
serializer
    book
        rating average (no need to embed a list of ratings)
        is_popular (a book that has some ratings and the rating avg >= 2 <-- dynamic attribute code

view: 
    create a new rating

url:
"""
class Rating(models.Model):
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="rating"
    )

    def __str__(self):
        return f'{self.id}: {self.value} for {self.book}'


# Creating a record
# Book.objects.create(title="test", price=9.99)

# Getting a record by primary key(pk)
# book = Book.objects.get(pk=3)
# we can perform operations on the returned object
# book.title = "test"
# book.price = 9.99

# this includes changes
# book.title = "new name"
# book.price = 100.0

# then save
# book.save()

"""
Deleting object
no need to save
book.delete()
"""

# Query
"""
Book.objects.filter(price__lt=9)
price__gte=9
price__range=(5,10)
Book.objects.filter(title__startswith='learn') <-- case insensitive
"""
