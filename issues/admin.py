from django.contrib import admin
from .models import *



@admin.register(Issue)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['username', 'book']
    prepopulated_fields = {'slug': ('username',)}

    

    