from django.urls import path

from products.views import (ProductDetailSlugView, ProductDetailView,
                            ProductListView)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path(
        "<slug>/",
        ProductDetailSlugView.as_view(),
        name="detail",
    ),
]
