from django.contrib import admin
from . models import Song, Watchlater, History

# Register your models here.

admin.site.register(Song)
admin.site.register(Watchlater)
admin.site.register(History)