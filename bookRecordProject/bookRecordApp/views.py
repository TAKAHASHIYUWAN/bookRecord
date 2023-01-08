from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from bookRecordApp.models import Book , Category

from .image_search.image_search import isbnSearch,imageSearch
from .price_search.bookoff_price import bookoff_search
from .price_search.valuebooks_price import valuebooks_search




class BookList(ListView):

    model = Book
    context_object_name = 'books'


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all
        # context['book'] =  context['book'].filter(user=self.request.user)
        return context
    # context_object_name は htmlのfor文内で使う。 for book in object_list を for book in book_list

    

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['book'] = context['book'].filter(user=self.request.user)

        return context
    """

# Create your views here.
class BookPrice(LoginRequiredMixin,DetailView):
    model = Book
    field = '__all__'
    context_object_name = 'book'
    template_name = 'bookRecordApp/book_price.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        book = Book.objects.values('title','auther').get(title=context['book'])
        """
        Model名.objectsでは欲しいものをvalueで指定する。
        """
        title , author = book['title'],book['auther']
        bookoff = bookoff_search(workname=title,authername=author)
        valuebooks = valuebooks_search(workname=title,authername=author)
        context['book_price'] ={
            'title' : title,
            'bookoff' : {'usedOrNew' : bookoff['usedOrNew'], 'price' : bookoff['price'],'url' : bookoff['url']},
            'valuebooks' : {'usedOrNew' : valuebooks['usedOrNew'], 'price' : valuebooks['price'], 'url' : valuebooks['url']}
        }
        print(context,title,author,bookoff,valuebooks)
        
        return context

class BookDetail(LoginRequiredMixin,DetailView):
    model = Book
    field = '__all__'
    context_object_name = 'book'


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all
        
        return context

    

class BookCreate(LoginRequiredMixin,CreateView):
    model = Book
    fields = ['title','auther','description','buy','read','review']
    success_url = reverse_lazy('books')

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all
        return context

    

class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all
        book_title = str(context['book'])
        images = imageSearch(isbnSearch(book_title))
        context['images'] = images
        return context

class BookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookListLogin(LoginView):
    fields = '__all__'
    template_name = 'bookRecordApp/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('books')

class RegistorBookRecordApp(FormView):
    template_name = 'bookRecordApp/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('books')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        if user is not None :
            login(self.request , user)
        return super().form_valid(form)