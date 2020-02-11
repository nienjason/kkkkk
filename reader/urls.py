from django.urls import path
from .views import *

urlpatterns = [
    path('', ReaderList.as_view(), name='reader_list'), 
    path('add/', ReaderAdd.as_view(), name='reader_add'),
    path('<int:pk>/', ReaderView.as_view(), name='reader_view'), 
    path('<int:pk>/edit/', ReaderEdit.as_view(), name='reader_edit'),
    path('<int:pk>/delete/', ReaderDelete.as_view(), name='reader_delete'),
]