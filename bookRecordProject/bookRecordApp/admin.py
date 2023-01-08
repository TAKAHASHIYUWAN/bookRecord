from django.contrib import admin
from bookRecordApp.models import Book,Category


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
    

admin.site.register(Book,BookAdmin)
admin.site.register(Category)
