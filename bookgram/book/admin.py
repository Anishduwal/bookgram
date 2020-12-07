from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = list_display = ("title","name","date")


admin.site.register(Book, BookAdmin)