from django.contrib import admin
from models import Entry, Budget, Category


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'budget', 'pub_date', 'amount', 'tax_included']
    prepopulated_fields = {'slug': ['title']}


class EntryInline(admin.TabularInline):
    model = Entry
    fields = ['title', 'budget', 'amount', 'tax_included', 'pub_date']
    extra = 1


class BugdetAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pub_date', 'amount']
    prepopulated_fields = {'slug': ['title']}
    inlines = [EntryInline]


class BudgetInline(admin.TabularInline):
    model = Budget
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    inlines = [BudgetInline]

admin.site.register(Entry, EntryAdmin)
admin.site.register(Budget, BugdetAdmin)
admin.site.register(Category, CategoryAdmin)


