from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin

# Register your models here.


from import_export import resources
from book.models import Book

from import_export.fields import Field

class BookResource(resources.ModelResource):
    published = Field(attribute='name', column_name='Imagen')
    
    name = Field(attribute='NAME', column_name='NAME')
    

    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource


admin.site.register(Book, BookAdmin)