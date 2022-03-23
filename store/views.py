from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Category,UserSignUp
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout

# Create your views here.
def home(request):
    prod= Product.objects.all()
    cat= Category.objects.all()
    print('you are : ' ,request.session.get('emailId'))
    print('you are : ' ,request.session.get('user_id'))
    data= {
        'products': prod,
        'category': cat,
    }
    return render(request, 'home.html', data)

def category(request, cat_id):
    category=Product.objects.filter(category=cat_id)
    data= {
        'cate': category,
    }
    # print(cat)
    return render(request, 'cat.html', data )


def sign_up(request):
    if request.method== 'POST':
        u_name= request.POST['email']
        pwd= request.POST['password']
        hashpwd= make_password(pwd)
        f_pwd= request.POST['f_password']
        data= {
            'u_name': u_name
        }
        if u_name and pwd and f_pwd !='':
            if pwd == f_pwd:
                if len(pwd)>=3:
                    querySave=UserSignUp(u_name=u_name, pwd=hashpwd)
                    querySave.save()
                    return redirect('signIn')
                else:
                    messages.info(request, "Password should be 8 charaters")
                    # print("length error")
                    return render(request, 'signup.html', data)
            else:
                messages.info(request, "Password doesn't match")
                return render(request, 'signup.html', data)
        else:
            messages.info(request, "All fields are required")
            return render(request, 'signup.html', data)
    else:
        return render(request, 'signup.html')


def sign_in(request):
    if request.method== 'POST':
        u_name= request.POST.get('user_name')
        password = request.POST.get('password')
        userData= UserSignUp.get_email(u_name)
        if userData:
            flag= check_password(password, userData.password)
            if flag:
                request.session['emailId']= userData.u_name
                request.session[' user_id']= userData.id
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

def log_out(request):
    logout(request)
    return redirect('home')