from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('add/', BookAdd.as_view(), name='book_add'), 
    path('<int:pk>/', BookView.as_view(), name='book_view'),
    path('<int:pk>/edit/', BookEdit.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
]
