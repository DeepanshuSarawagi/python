from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
admin.site.register(Tag)
