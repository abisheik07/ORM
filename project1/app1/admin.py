from django.contrib import admin

# Register your models here.
from .models import Movies, MoviesAdmin
admin.site.register(Movies,MoviesAdmin)