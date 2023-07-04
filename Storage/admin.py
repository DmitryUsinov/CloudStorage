from django.contrib import admin

# Register your models here.
from .models import *


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'slug')
    list_display_links = ('id', )
    prepopulated_fields = {'slug': ('title', )}

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(File, FileAdmin)