from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)


admin.site.register(Book)  # This is how you register the models in admin site
