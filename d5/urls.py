from django.contrib import admin
from django.urls import path, include

from library import views
from library.views import AuthorEdit, AuthorList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publisher),
    path('library/', include('library.urls')),
]