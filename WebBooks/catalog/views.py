from django.shortcuts import render
from .models import Book, Author, Bookinstance
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_instance = Bookinstance.objects.all().count()
    num_instance_available = Bookinstance.objects.filter(status__exact=2).count()
    num_author = Author.objects.count()
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instance': num_instance,
                           'num_instance_available': num_instance_available,
                           'num_authors': num_author,
                           'num_visitors': num_visitors}, )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
