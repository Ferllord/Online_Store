from django.contrib import admin

from .models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity','category')
    fields = ('name','description' ,'price', 'quantity', 'image','category')
    readonly_fields = ('description',)
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    readonly_fields = ('created_timestamp',)
    fields = ('product','quantity','created_timestamp')
    extra = 0