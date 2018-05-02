from django.contrib import admin
from . import models
import decimal

admin.site.site_header = "Coretabs Online Shop Administration"
admin.site.index_title = ""

def make_price_zero(modeladmin, request, queryset):
    queryset.update(price=0)
make_price_zero.short_description = "Make selected products free"

def discount(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * decimal.Decimal('0.8')
        product.save()
discount.short_description = 'Apply 20%% DISCOUNT'
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
   date_hierarchy = 'created_at'
   search_fields = ['name']
   list_display = ('name', 'price', 'stock', 'category',)
   list_filter = ('created_at', 'category',)
   actions = [make_price_zero, discount]

 
@admin.register(models.Category) # This will add Category to admin 
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ['name']
    date_hierarchy = 'created_at'
