from django.contrib import admin
from store.models import Product, Category, UserSignUp

# Register your models here.
class ProductView(admin.ModelAdmin):
    list_display=('name','category', 'price', 'img')
admin.site.register(Product, ProductView)

# class CategoryView(admin.ModelAdmin):
#     list_display=('category')
admin.site.register(Category)
class userView(admin.ModelAdmin):
    list_display=('id', 'u_name', 'date')
admin.site.register(UserSignUp, userView)