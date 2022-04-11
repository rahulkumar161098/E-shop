from optparse import Values
from re import U
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Category,UserSignUp, Address
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
from .templatetags.cart import total_price
import razorpay  
# payment getway

# Create your views here.
def home(request):

    # add to cart
    if request.method=='POST':
        product_id= request.POST.get('pro_id')
        remove= request.POST.get('remove')
        cart= request.session.get('cart')
        if cart:
            quantity= cart.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1
            else:
                cart[product_id] = 1
        else:
            cart= {}
            cart[product_id] = 1
        request.session['cart']= cart
        print(cart)
        # print("Product id to add in cart", product_id)

    cart= request.session.get('cart')
    if not cart:
        request.session.cart= {}

    # showing all items 
    prod= Product.objects.filter(category=1)

    # filtered by mobiles
    filter_by_mobile= Product.objects.filter(category=4)
    # print('filer_by_mobile : ',filter_by_mobile)

    # deal of the day
    deal_of_the_day= Product.objects.filter(mark='DD')
    print('dealof the day', deal_of_the_day)
    
    # all category
    cat= Category.objects.all()

    print('user id : ' ,request.session.get('user_id'))
    print('you are : ' ,request.session.get('email'))

    # creating a dic
    data= {
        'products': prod,
        'category': cat,
        'filter_by_mobile': filter_by_mobile,
    }
    return render(request, 'home.html', data)
    # return HttpResponse('hello')

def category(request, cat_id):
    category=Product.objects.filter(category=cat_id)
    data= {
        'cate': category,
    }
    # print(cat)
    return render(request, 'cat.html', data )


def sign_up(request):
    if request.method== 'POST':
        # user inputes
        u_name= request.POST['email']
        pwd= request.POST['password']
        hashpwd= make_password(pwd)
        f_pwd= request.POST['f_password']
        data= {
            'u_name': u_name
        }
        # checking all fields are filled
        if u_name and pwd and f_pwd !='':
            # cheking user existance
            if UserSignUp.objects.filter(u_name = u_name):
                messages.info(request,'User already exist Please try another!')
                return render(request, 'signup.html')
            else:
                # matching password
                if pwd == f_pwd:
                    #set password length
                    if len(pwd)>=3:
                        querySave=UserSignUp(u_name=u_name, password=hashpwd)
                        querySave.save()
                        return redirect('signIn')
                    else:
                        messages.info(request, "Password should be 8 charaters!")
                        # print("length error")
                        return render(request, 'signup.html', data)
                else:
                    messages.info(request, "Password doesn't match!")
                    return render(request, 'signup.html', data)
        else:
            messages.info(request, "All fields are required!")
            return render(request, 'signup.html', data)
    else:
        return render(request, 'signup.html')


def sign_in(request):
    if request.method== 'POST':
        # user inputs
        u_name= request.POST.get('user_name')
        password = request.POST.get('password')
        userData= UserSignUp.get_email(u_name)
        # validating user
        if userData:
            flag= check_password(password, userData.password)
            if flag:
                # storing session
                request.session['user_id']= userData.id
                request.session['email']= userData.u_name
                return redirect('home')
            else:
                messages.info(request, 'Invalid password !')
                return render(request, 'sign_in.html')
        else:
            messages.info(request, 'Invalid user name')
            return render(request, 'sign_in.html')

        # return render(request, 'sign_in.html')   
    else:
        return render(request, 'sign_in.html')

# user logout function
def log_out(request):
    logout(request)
    return redirect('home')


#View cart
def cart_views(request):
    cart=list(request.session.get('cart').keys())
    cart_product=Product.objects.filter(id__in=cart)
    print(cart_product)
    cart_items={
        'cart_product': cart_product,
    }
    # checking items in card
    # print("cart keys", cart)
    # print(len(cart))
    # print('cart products :',cart_product)
    if len(cart) ==0:
        # return HttpResponse("no product in cart")
        return render(request, 'no_product_in_cart.html')
    else:
        return render(request, 'cart.html', cart_items)


#check out
def check_out(request):
    # show user address
    u_id=request.session.get('user_id')

    # print(u_id)
    cart= list(request.session.get('cart').keys())
    print('keys',cart)
    
    userAddress= Address.objects.filter(user_id=u_id)
    # print(userAddress)

    # count no of a paticular product
    items_of_a_product= request.session.get('cart')

    # Count all product
    cart_all_items= request.session.get('cart')
    total_no_of_items=len(cart_all_items)

    # delivery charge
    delivey_charge= 50

    # get total amount 
    cart_product=Product.objects.filter(id__in=cart)
    print("card",cart_product)
    allAddress={
        'userAddress': userAddress,
        'cart' : cart,
        'cart_product': cart_product,
        'total_no_of_items': total_no_of_items,
        'items_of_a_product': items_of_a_product,
        'delivey_charge': delivey_charge
    }
    # save address of the user
    if request.method== 'POST':
        user=request.POST['userid']
        name= request.POST['name']
        mobile= request.POST['mobile']
        address= request.POST['address']
        pin= request.POST['pin']
        lend_mark= request.POST['lend_mark']
        city= request.POST['city']
        state= request.POST['state']

        # form validations

        set_address= Address(user_id=user, name=name, mobile=mobile, local_address=address, city=city, zip_code=pin, lend_mark=lend_mark, state= state)
        set_address.save()
        return redirect('checkOut')
    return render(request, 'orders/order.html', allAddress)


# show on product
def product_details(request, id):
    details_page= Product.objects.get(id=id)


    return render(request, 'show_one_pro.html', {'details_page': details_page})


# payment function or fimall process
def payment(request):
   
    cart= request.session.get('cart').keys()
    cart1= request.session.get('cart')
    print(cart1)
    # print(get('cart'))
    total_items_in_cart=len(cart)
    print("items in cart: ", cart)
    cart_product=Product.objects.filter(id__in=cart)
    # price= total_price(product_id, cart)
    # print(price)
    delivery_charge= 50
    cart_info= {
        'total_items_in_cart': total_items_in_cart,
        'cart_product' : cart_product,
        'delivery_charge' : delivery_charge,
        'cart1':cart1
    }
    return render(request, 'orders/payment.html', cart_info)


#payment gateway (RarorPay)
# import razorpay
# client = razorpay.Client(auth=("", ""))


# amount= 100,
# currency= "INR",
# client = razorpay.Client(auth=("rzp_test_3Xjh9rRVSDJ3Lu", "HzIgyX5NwXq2BnUkx4ot3uLx"))
# payment= client.order.create({amount: 'amount', 'currency': "INR",'payment_capture': '0'})
    # "receipt": "receipt#1",
    # "notes": {
    #     "key1": "value3",
    #     "key2": "value2"
    # }

# import razorpay
client = razorpay.Client(auth=("rzp_test_3Xjh9rRVSDJ3Lu", "HzIgyX5NwXq2BnUkx4ot3uLx"))

amount= 100,
currency= "INR",

# payment= client.order.create({'amount': amount, 'currency': "INR",'payment_capture': '0'})
# client.order.create(data=DATA)