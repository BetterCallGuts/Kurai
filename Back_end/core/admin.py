from django.contrib import admin
from .models import Category, Product, ProductImages, Review, Cart, Pages


# Inlines 
class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 0

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class CartInline(admin.TabularInline):
    model = Cart
    extra = 0
# Admin style
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ReviewInline, CartInline]

class PagesAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product , ProductAdmin)

admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Pages , PagesAdmin)