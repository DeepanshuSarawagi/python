from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tags",)
    list_display = ("title", "author", "date",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
