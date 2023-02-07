from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Author, Book
from .forms import BookForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView


class Home(TemplateView):
    template_name = "home.html"


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_create.html'
    success_url = '/books/'


class ViewBook(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class UpdateBook(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = '__all__'
    success_url = '/books/'


class DeleteBook(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books')

    def post(self, request, *args, **kwargs):
        if request.POST["cancel"]:
            return redirect('/books/')
        else:
            return super(DeleteBook, self).post(request, *args, **kwargs)
# Create your views here.


# def home(request):
 #   return render(request, "home.html")


# def book(request):
 #   book_list = [
  #      'book1', 'book2', 'book3', 'book4', 'book5'
   # ]
    # context = {
     #   'book_list': book_list
    # }
    # return render(request, 'books.html', context)


# def details(request, book_id=1):
 #   if book_id == None:
  #      return HttpResponse('no book_id')
   # else:
    #    book_info = f"This is book {book_id}'s detail page"
     #   context = {
      #      'book_info': book_info
       # }
        # return render(request, 'books_details.html', context)
