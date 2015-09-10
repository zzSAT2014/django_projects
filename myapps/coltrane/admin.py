# Register your models here.
from django.contrib import admin
from models import Entry, Category, Link


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ("title", "pub_date", "author")


class LinkAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)
