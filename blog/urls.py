from django.conf.urls import url
from .views import PostList, post_share, post_detail

app_name = 'blog'
urlpatterns = [
    # post views
    url(r'^$', PostList.as_view(), name='post_list'),
    url(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        post_detail,
        name='post_detail'
    ),
    url(r'^(?P<post_id>\d+)/share/$', post_share, name='post_share'),
]