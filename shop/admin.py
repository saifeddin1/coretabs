from django.contrib import admin
from . import models


def make_price_zero(modeladmin, request, queryset):
    queryset.update(price=0)

make_price_zero.short_description = "Make selected products free"

def make_discount(modeladmin, request, queryset):
    queryset.update(price=-20)
    

make_discount.short_description = "Make a 20 percent discount on selected items"

admin.site.site_header = "Coretabs Online Shop Administration"
admin.site.index_title = ""
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
   date_hierarchy = 'created_at'
   search_fields = ['name']
   list_display = ('name', 'price', 'stock', 'category',)
   list_filter = ('created_at', 'category',)
   actions = [make_price_zero, make_discount]

 
@admin.register(models.Category) # This will add Category to admin 
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ['name']
    date_hierarchy = 'created_at'