from django.urls import path

from search.views import SearchProductListView

app_name = "search"

urlpatterns = [
    path("", SearchProductListView.as_view(), name="search_list"),
]
