from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductListView(ListView):
    template_name = "search/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get("query", None)
        if query:
            return Product.objects.search(query)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get("query", None)
        return context
