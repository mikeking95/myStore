from django.db.models import Q

from django.contrib.auth.mixins import  (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.views.generic import ListView, DetailView

from .models import Book, Product

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'products.special_status'

class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

class FeaturedProductsView(ListView):
    model = Product
    context_object_name = 'featured_list'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('#featured')
        return Product.objects.all()
