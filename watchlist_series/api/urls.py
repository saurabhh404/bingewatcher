from django.urls import path, include
from watchlist_series.api.views import entire_list, series_details

urlpatterns = [
    path("list/", entire_list, name="entire_list"),
    path("<int:pk>", series_details, name="series_details"),
]
