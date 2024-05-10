from django.contrib import admin

from watchlist.models import Review
from watchlist.models import StreamPlatform
from watchlist.models import Watchlist

# Register your models here.

admin.site.register(Watchlist)
admin.site.register(StreamPlatform)
admin.site.register(Review)
