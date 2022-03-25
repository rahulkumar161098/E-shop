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

class UserAddress(models.Model):
    user= models.ForeignKey(UserSignUp, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    mobile= models.CharField(max_length=12)
    local_address= models.CharField(max_length=100)
    zip_code= models.CharField(max_length=6)
    lend_mark= models.CharField(max_length=50)
    city= models.CharField(max_length=30)
    state= models.CharField(max_length=30)
    date= models.DateTimeField(auto_now_add=True)


class orders(models.Model):
    user= models.ForeignKey(UserSignUp, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    price= models.IntegerField()
    date= models.DateTimeField(auto_now_add=True)