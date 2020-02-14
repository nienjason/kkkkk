from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from reader.models import Reader
from book.models import Book
from datetime import datetime
from .models import Log

# 借閱記錄列表
class LogList(LoginRequiredMixin, ListView):
    model = Log
    ordering = ['-checkout']
    paginate_by = 20

# 借書階段1：選擇讀者
class CheckoutReader(LoginRequiredMixin, ListView):
    model = Reader
    paginate_by = 20
    template_name = 'log/checkout_reader_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            readers = Reader.objects.filter(realname__icontains=query)
        else:
            readers = Reader.objects
        return readers.order_by("realname")
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

# 借書階段2：選擇書籍
class CheckoutBook(LoginRequiredMixin, ListView):
    model = Book
    paginate_by = 7
    template_name = 'log/checkout_book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects
        return books.exclude(
            log__checkout__isnull=False, 
            log__returned__isnull=True
        ).order_by('title')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        curr_reader = Reader.objects.get(id=self.kwargs['rid'])
        ctx['query'] = self.request.GET.get('query') or ""
        ctx['reader'] = curr_reader
        ctx['borrowing'] = curr_reader.log_set.filter(
            returned__isnull=True
        ).select_related('book')
        return ctx

# 借書階段3：借書登錄
class CheckoutLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        reader = Reader.objects.get(id=self.kwargs['rid'])
        book = Book.objects.get(id=self.kwargs['bid'])
        log = Log(reader=reader, book=book)
        log.save()
        return reverse('checkout_book', kwargs={'rid': reader.id})

# 還書階段1：借閱中書籍列表
class ReturnBook(LoginRequiredMixin, ListView):
    model = Log
    paginate_by = 20
    template_name = 'log/return_book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            logs = Log.objects.filter(book__title__icontains=query)
        else:
            logs = Log.objects
        return logs.exclude(
            returned__isnull=False
        ).select_related('book', 'reader')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

# 還書階段2：還書登記
class ReturnLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        log = Log.objects.get(id=self.kwargs['lid'])
        log.returned = datetime.now()   # 填入歸還時間
        log.save()                      # 更新紀錄
        return reverse('return_book')
