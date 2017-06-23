from django.shortcuts import render
from books.models import Publisher, Author, Book
from django.views.generic import ListView, DetailView

# Create your views here.


class PublisherList(ListView):
    queryset = Publisher.objects.order_by('state_province')


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(publisher__name=context['publisher'].name)
        # context['book_list'] = Book.objects.filter(pk=self.kwargs[0].value)
        return context

