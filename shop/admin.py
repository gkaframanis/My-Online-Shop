from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    # Set prepopulated_fields to a dictionary mapping field names to the fields it should prepopulate from.
    # The main use for this functionality is to automatically generate the value for SlugField fields from one or more other fields
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category", "price", "stock", "available", "created", "updated"]
    list_filter = ["available", "created", "updated", "category"]
    # Every field in the list_editable should also exist in the list_display
    list_editable = ["price", "stock", "available"]
    prepopulated_fields = {"slug": ("name",)}
