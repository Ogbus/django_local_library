from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """view function for home page of site"""

    # generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # Number of visit to this view is counted in the session
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    num_instances = BookInstance.objects.all().count

    # available books (status = 'a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # the all() is applied by default
    num_authors = Author.objects.count()

    words_in_genre = Genre.objects.filter(name__exact='Thriller').count()
    words_in_books = Book.objects.filter(title__exact='hard').count()


    # dynamic page title
    page_title = 'Abuja Local Library'

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'words_in_books': words_in_books,
        'words_in_genre': words_in_genre,
        'page_title': page_title,
        'num_visits': num_visits,
    }

    # render the html template index.html with the data in the context available
    return render(request, 'index.html', context)

class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author