from django.contrib import admin
from .models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'status', 'in_stock',
    'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['in_stock']
    prepopulated_fields = {'slug':('title',)}
    

    