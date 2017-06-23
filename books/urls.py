from django.conf.urls import url
from books.views import PublisherList, PublisherDetail

app_name = 'books'
urlpatterns = [
    url(r'^publishers/$', PublisherList.as_view(), name='publishers'),
    url(r'^publisher/(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name='publisher'),
]