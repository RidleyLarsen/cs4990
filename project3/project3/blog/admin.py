from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'active', 'pub_date', 'published')
    list_filter = ('active', 'author')
    list_editable = ('active', )

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
