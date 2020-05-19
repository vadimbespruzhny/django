from django.contrib import admin
from my_first_site.note.models import Manufacturer, Product, Description
from django.contrib.auth.models import User

# Register your models here.

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# from import_export.fields import Field


# class ProductResource(resources.ModelResource):
#     class Meta:
#         model = Product
#         fields = ('id', 'name')
#         import_id_fields = ('name')


# class Product_Imp_Exp_Admin(ImportExportModelAdmin):
#     resource_class = ProductResource
#     list_display = ['name', 'category', 'price']


# admin.site.register(Product, Product_Imp_Exp_Admin)


class ProductAdmin(admin.ModelAdmin):
    model = Product


admin.site.register(Product, ProductAdmin)

class ProductItemInline(admin.TabularInline):
    model = Product
    list_display = ['name', 'color']


class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    list_display = [
        'name', 'country']
    inlines = [ProductItemInline]


class DescriptionAdmin(admin.ModelAdmin):
    model = Description


admin.site.register(Description, DescriptionAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
