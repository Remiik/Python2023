from django.contrib import admin
from .models import BlogPages
from .models import BlogPages, BlogPagesAdmin

admin.site.register(BlogPages, BlogPagesAdmin)