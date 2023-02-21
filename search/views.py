from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

class SearchProductListView(ListView):
    template_name = "search/list.html"
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get("query")
        if query:
            return Product.objects.filter(title__icontains=query)
