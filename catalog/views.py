from django.shortcuts import render, get_object_or_404
from catalog.Models.book import Book
from catalog.Models.bookinstance import BookInstance
from catalog.Models.author import Author
from django.views import generic


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'booklist.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['book'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authorList.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        return context


class AuthorDetailView(generic.DetailView):
    model = Book
    template_name = 'author.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['author'] = get_object_or_404(Author, pk=self.kwargs['pk'])
        return context
