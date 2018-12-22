from django.urls import path
from . import views

app_name = 'mybook'

urlpatterns = [
    path('book_create', views.book_create, name='book_create'),
    path('book_retrieve', views.book_retrieve, name='book_retrieve'),
]
