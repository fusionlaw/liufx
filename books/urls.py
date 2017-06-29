from django.conf.urls import url
from books.views import PublisherList, PublisherDetail, AuthorList, AuthorDetail, ContactView, AuthorCreate,\
    AuthorUpdate, AuthorDelete
from django.views.generic import TemplateView

app_name = 'books'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    url(r'^publishers/$', PublisherList.as_view(), name='publishers'),
    url(r'^publisher/(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name='publisher'),
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^author/(?P<pk>[0-9]+)$', AuthorDetail.as_view(), name='author'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'^author/(?P<pk>[0-9]+)/update/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'^author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
]