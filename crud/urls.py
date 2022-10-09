



from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/create/',views.book_create, name='book_create'),
    path('books/<int:id>/update/',views.book_update, name='book_update'),
    path('books/<int:id>/delete/',views.book_delete,name='book_delete'),

]