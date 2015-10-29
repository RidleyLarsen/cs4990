from django.contrib import admin
from .models import Tag, Note

admin.site.register(Note)
admin.site.register(Tag)
