from django.contrib import admin
from books.models import Book, Publisher, Author
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['publication_date', 'publisher']
    list_display = ['title', 'display_authors', 'publisher', 'publication_date']
    list_per_page = 5

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author)