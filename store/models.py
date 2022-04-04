from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField()
    category= models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    img= models.FileField(upload_to='product_img')
    des= models.CharField(max_length=200)



class Category(models.Model):
    category= models.CharField(max_length=30)

    def __str__(self):
        return self.category


class UserSignUp(models.Model):
    u_name= models.CharField(max_length=50)
    password= models.CharField(max_length=255)
    date= models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def get_email(u_name):
        return UserSignUp.objects.get(u_name=u_name)

    def __str__(self):
        return self.u_name

class Address(models.Model):
    user_id= models.CharField(max_length=10)
    name= models.CharField(max_length=50)
    mobile= models.CharField(max_length=12)
    local_address= models.CharField(max_length=100)
    zip_code= models.CharField(max_length=6)
    lend_mark= models.CharField(max_length=50)
    city= models.CharField(max_length=30)
    state= models.CharField(max_length=30)
    date= models.DateTimeField(auto_now_add=True)
     
    # def __str__(self):
    #     return self.user_id


class orders(models.Model):
    DELIVERY_STATUS=[
        ('PN', 'Panding'),
        ('AC', 'Accepted'),
        ('OD', 'Out for Delivery'),
    ]
    userId= models.ForeignKey(UserSignUp, on_delete=models.CASCADE, default=0,null=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, default=0, null=True)
    addressId= models.ForeignKey(Address, on_delete=models.CASCADE, default=0, null=True)
    cart_product= models.CharField(max_length=500, null=True, default=0)
    total_amoumt= models.IntegerField(default=0)
    status= models.CharField(choices=DELIVERY_STATUS, max_length=10, default='panding')
    date= models.DateTimeField(auto_now_add=True, null=True)