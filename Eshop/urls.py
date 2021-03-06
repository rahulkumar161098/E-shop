from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('sign-up/', views.sign_up, name="signUp"),
    path('sign-in/', views.sign_in, name="signIn"),
    path('category/<int:cat_id>', views.category),
    path('logout/', views.log_out, name='log_out'),
    path('cart/', views.cart_views, name='cart'),
    path('check_out/', views.check_out, name="checkOut"),
    path('payment/', views.payment, name='payment_link'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('all_mobiles/', views.all_product_of_mobiles, name='all_mobile_product'),
    path('search/', views.search, name="search")
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
