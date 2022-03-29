from django.contrib import admin
from store.models import Product, Category, UserSignUp, Address, orders

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

#user address views
class UserAddress(admin.ModelAdmin):
    list_display=('user_id', 'name', 'mobile', 'state',  'zip_code', 'date')
admin.site.register(Address, UserAddress)

#order views
class OrderViews(admin.ModelAdmin):
    list_diaplay=('user', 'product', 'date')
admin.site.register(orders, OrderViews)