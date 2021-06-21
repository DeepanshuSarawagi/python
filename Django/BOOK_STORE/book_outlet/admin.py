from django.contrib import admin
from .models import Book, Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "rating", "author")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)  # This is how you register the models in admin site
admin.site.register(Author, AuthorAdmin)
