from django.conf.urls import url
from .views import dashboard
from django.contrib.auth import views

urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', dashboard, name='dashboard'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout-then-login/$', views.logout_then_login, name='logout_then_login'),
    # change password urls
    url(r'^password-change/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

