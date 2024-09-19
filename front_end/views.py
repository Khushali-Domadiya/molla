from django.shortcuts import render,redirect
from admin_side.models import *
from front_end.models import *

# Create your views here.
def home(request):
    row = ''
    if 'user_id' in request.session:
        row = signup.objects.filter(id=request.session['user_id']).first()
    sld = slide.objects.all()
    prd = product.objects.order_by().all()
    recent = product.objects.order_by('-id').all()[:8]
    return render(request,'index.html',{'sld':sld,'prd':prd,'rcnt':recent,'row':row})

def registration(request):
    if 'save' in request.POST:
        frm = SIGNUP(request.POST,request.FILES)
        frm.save()
    return render(request,'signup.html')

def user_login(request):
    msg = ""
    row = ""
    data = ""
    if 'save' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        data = signup.objects.filter(email=email,password=password)
        print(data)
        print(data.count())
        if data.count() == 1:
            row = data.first()
            print(row)
            if row.status == 1:
                request.session['user_id'] = row.id
            else:
                msg = "User HasbeeN BlockeD"
        else:
            msg = "Please Enter Valid E-Mail Or Password"
    return render(request,'login.html',{'msg':msg})

def user_logout(request):
    del request.session['user_id']
    return render('/')

def about(request):
    return render(request,'about.html')
    
def shop(request):
    return render(request,'shop.html')

def cart_ft(request):
    return render(request,'cart.html')

def add_cart(request,cart_id):
    prd = product.objects.filter(id=cart_id).all()
    if prd :
        user_id = signup.objects.filter(id=request.session['user_id']).first()
        prdInfo = product.objects.filter(id=cart_id).get()
        frm = CART(
            user_id=user_id,
            product_id=prdInfo,
            prize=prdInfo.prize,
            quantity=1,
            sub_total=prdInfo.prize
        )
        frm.save()
    return redirect('/shop')

def checkout(request):
    return render(request,'checkout.html')

def wishlist(request):
    wishlist_prd = ""
    if 'user_id' in request.session:
        wishlist_prd = WISHLIST.objects.filter(user_id=request.session['user_id']).all()
        # print(wishlist_prd)
    return render(request,'wishlist.html',{'wishlist_prd':wishlist_prd})

def add_wishlist(request,wish_id):
    prd = product.objects.filter(id=wish_id).all()
    if prd :
        user_id = signup.objects.filter(id=request.session['user_id']).first()
        prdInfo = product.objects.filter(id=wish_id).get()
        frm = WISHLIST(
            user_id=user_id,
            product_id=prdInfo,
            prize=prdInfo.prize,
            quantity=1,
            sub_total=prdInfo.prize
        )
        frm.save()
    return redirect('/shop')

def faq(request):
    return render(request,'faq.html')

def category_all(request):
    return render(request,'category.html')

def single_product(request):
    return render(request,'single_product.html')

def dashboard(request):
    return render(request,'dashboard.html')