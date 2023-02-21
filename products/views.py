from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Product


# featured
class ProductFeaturedListView(ListView):
    template_name = "products/featured_list.html"
    queryset = Product.objects.all().featured()

    def get_queryset(self):
        req = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured_detail.html"
    queryset = Product.objects.all().featured()


# basic
class ProductListView(ListView):
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data()

        return super().get_context_data(**kwargs)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()


# slug
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_object(self, *a, **kva):
        req = self.request
        slug = self.kwargs.get("slug")
        instance = get_object_or_404(Product, slug=slug)

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            return Product.objects.filter(slug=slug).first()

        return instance
