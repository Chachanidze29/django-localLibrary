from django.contrib import admin
from catalog.Models.book import Book
from catalog.Models.bookinstance import BookInstance
from catalog.Models.genre import Genre
from catalog.Models.author import Author

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)