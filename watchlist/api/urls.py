from django.urls import path

from watchlist.api.views import ReviewCreate
from watchlist.api.views import ReviewDetails
from watchlist.api.views import ReviewList
from watchlist.api.views import StreamPlatformDetailsView
from watchlist.api.views import StreamPlatformListView
from watchlist.api.views import WatchlistDetailsView
from watchlist.api.views import WatchlistListView

urlpatterns = [
    path(
        "list/",
        WatchlistListView.as_view(),
        name="watch-list",
    ),
    path(
        "<int:pk>",
        WatchlistDetailsView.as_view(),
        name="watch-list-detail",
    ),
    path(
        "stream/",
        StreamPlatformListView.as_view(),
        name="stream-platform-list",
    ),
    path(
        "stream/<int:pk>/",
        StreamPlatformDetailsView.as_view(),
        name="stream-platform-detail",
    ),
    path(
        "review/<int:pk>/",
        ReviewDetails.as_view(),
        name="review-detail",
    ),
    path(
        "<int:pk>/reviews/",
        ReviewList.as_view(),
        name="review-list",
    ),
    path(
        "<int:pk>/review/create/",
        ReviewCreate.as_view(),
        name="review-list",
    ),
]
