from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'level', 'created_at')
    list_filter = ('level', 'created_at')
    search_fields = ('word', 'definition')
    ordering = ('word',)
    
    # Make it easier to add words
    fields = ('word', 'definition', 'example', 'level')
