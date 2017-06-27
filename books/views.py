from django.shortcuts import render
from books.models import Publisher, Author, Book
from django.views.generic import ListView, DetailView
from books.forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
    fields = ['salutation']
    fields = ['email']
    fields = ['headshot']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    fields = ['salutation']
    fields = ['email']
    fields = ['headshot']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


class PublisherList(ListView):
    queryset = Publisher.objects.order_by('state_province')


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(publisher__name=context['publisher'].name)
        # context['book_list'] = Book.objects.filter(pk=self.kwargs[0].value)
        return context


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'http://www.baidu.com/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

