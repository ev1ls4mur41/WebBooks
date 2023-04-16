from ..catalog import views
from django.contrib import admin
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    path('admin/', admin.site.urls)
]
