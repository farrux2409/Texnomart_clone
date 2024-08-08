from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Category)
class GroupsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    search_fields = ['category_name']
    prepopulated_fields = {'slug': ('category_name',)}
    list_filter = ['category_name', ]


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['product_name', 'price', ]
    search_fields = ['product_name', ]
    prepopulated_fields = {'slug': ('product_name',), }
    list_filter = ['price', ]


admin.site.register(Image)
admin.site.register(ProductAttribute)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Comment)
