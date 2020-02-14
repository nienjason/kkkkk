from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from log.models import Log

# Create your views here.
class BookList(LoginRequiredMixin, ListView):   # 圖書列表
    model = Book    
    paginate_by = 8

class BookView(LoginRequiredMixin, DetailView): # 檢視圖書
    model = Book

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['log_list'] = Log.objects.filter(
            book=self.object, 
        ).order_by('-id').select_related('reader')
        return ctx

class BookAdd(LoginRequiredMixin, CreateView):  # 新增圖書
    model = Book
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')

class BookEdit(LoginRequiredMixin, UpdateView): # 編輯圖書
    model = Book
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('book_list')

class BookDelete(LoginRequiredMixin, DeleteView):   # 刪除圖書
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book_list')