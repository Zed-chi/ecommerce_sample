from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView
from django.db.models import Q

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