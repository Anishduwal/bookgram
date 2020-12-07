from django.shortcuts import render,redirect,  get_object_or_404
from .models import Book
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        description = request.POST['desc']
        new_book = Book.objects.create(name = name, title = title, description = description)
        new_book.save()
    books = Book.objects.all()
    return render(request, 'home.html',{"books":books})

def update(request, id):
    obj = get_object_or_404(Book, id = id)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['desc']
        obj.title = title
        obj.description = description
        try:
            obj.save()
        finally:
            return redirect("index")
    return render(request, 'update.html',{"obj":obj})

def delete(request,id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
    finally:
        return redirect("index")
