from django.contrib import admin
from main.models import Product,ProductImage,Category,Cart,ProductToCart

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]
    list_display = ('title',)
    
    
    
    
class ProductToCartInline(admin.TabularInline):
    model = ProductToCart
    extra=0
class CartAdmin(admin.ModelAdmin):
    inlines = [ ProductToCartInline, ]
    list_display = ('user',)

    
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Cart,CartAdmin)