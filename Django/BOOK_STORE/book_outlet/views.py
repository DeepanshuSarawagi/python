from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")  # sorting the list of books based on rating in Descending order
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))  # We are using the built-in Aggregate() and using the Avg class, we
    # are calculating the average rating. rating is the attribute of Book class in models.py

    return render(request, "book_outlet/index.html", context={
        "books": books,
        "total_num_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # book = Book.objects.get(pk=id)  # pk is the default named keyword argument which means primary key
    book = get_object_or_404(Book, slug=slug)  # named keyword arg slug is the attribute in the models and value is the
    # parameter slug passed when book_detail is called
    return render(request, "book_outlet/book-detail.html", context={
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })
