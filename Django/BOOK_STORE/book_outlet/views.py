from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", context={
        "books": books
    })


def book_detail(request, slug):
    # book = Book.objects.get(pk=id)  # pk is the default named keyword argument which means primary key
    book = get_object_or_404(Book, slug=slug)  # slug is the parameter and value slug is the attribute in models
    return render(request, "book_outlet/book-detail.html", context={
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })
