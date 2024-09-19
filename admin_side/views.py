from django.shortcuts import render,redirect
from admin_side.models import *
# Create your views here.
def admin_dashboard(request):
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
    else:
        return redirect('/myadmin/signin')
    return render(request,'index_admin.html',{'row':row})

def admin_signin(request):
    if 'save' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        data = sign_up.objects.filter(email=email,password=password)
        print(data.count())
        if data.count() == 1:
            row =  data.first()
            request.session['admin_id']=row.id
            return redirect('/myadmin/dashboard')
    return render(request,'admin_sign-in.html')

def admin_signup(request):
    frm = SIGN_UP
    if 'save' in request.POST:
        frm = SIGN_UP(request.POST, request.FILES)
        frm.save()
    return render(request,'admin_sign-up.html')

def admin_logout(request):
    del request.session['admin_id']
    return redirect('/myadmin/signin')

# def category(request):
def add_slide(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        if 'save' in  request.POST:
            frm = SLIDE(request.POST,request.FILES)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_slide.html',{'row':row})

def update_slide(request,edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = slide.objects.filter(id=edit).get()
        if 'save' in request.POST:
            frm = SLIDE(request.POST,request.FILES,instance=data)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_slide.html',{'row':row,'data':data})

def delete_slide(request,delt):
    data = slide.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_slide')

def manage_slide(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = slide.objects.all()    
    else:
        return redirect('/myadmin/signin')
    
    return render(request,'manage_slide.html',{'row':row,'data':data})

def add_brand(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        if 'save' in request.POST:
            frm = BRAND(request.POST,request.FILES)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_brand.html',{'row':row})

def manage_brand(request):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = brand.objects.all()
    else:
        return redirect('/myadmin/signin')
    return render(request,'manage_brand.html',{'row':row,'data':data})

def update_brand(request,edit):
    row = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = brand.objects.filter(id=edit).get()
        if 'save' in request.POST:
            frm = BRAND(request.POST,request.FILES,instance=data)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_brand.html',{'row':row})

def delete_brand(request,delt):
    data = brand.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_brand')

def add_category(request):
    row = ' '
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        if 'save' in request.POST:
            frm = CATEGORY(request.POST,request.FILES)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_category.html',{'row':row})

def manage_category(request):
    row = ' '
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = category.objects.all()
    else:
        return redirect('/myadmin/signin')
    return render(request,'manage_category.html',{'row':row,'data':data})

def update_category(request,edit):
    row = ' '
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = category.objects.filter(id=edit).get()
        if 'save' in request.POST:
            frm = CATEGORY(request.POST,request.FILES,instance=data)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_category.html',{'row':row})

def delete_category(request,delt):
    data = category.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_category')

def add_subcategory(request):
    row = ''
    catgry = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        catgry = category.objects.all()
        if 'save' in request.POST:
            frm = SUB_CATEGORY(request.POST,request.FILES)
            frm.save()
    return render(request,'add_subcategory.html',{'row':row,'cat':catgry})

def manage_subcategory(request):
    row = ''
    data = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = sub_category.objects.all()
    else:
        return redirect('/myadmin/signin')
    return render(request,'manage_subcategory.html',{'row':row,'data':data})

def update_subcategory(request,edit):
    row = ""
    data = ""
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = sub_category.objects.filter(id=edit).get()
        if 'save' in request.POST:
            frm = SUB_CATEGORY(request.POST,request.FILES,instance=data)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_subcategory.html',{'row':row})

def delete_subcategory(request,delt):
    data = sub_category.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_subcategory')

def add_product(request):
    row = ""
    brnd = ""
    cat = ""
    subcat = ""
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        brnd = brand.objects.all()
        cat = category.objects.all()
        subcat = sub_category.objects.all()
        if 'save' in request.POST:
            frm = PRODUCT(request.POST,request.FILES)
            frm.save()
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_product.html',{'row':row,'brnd':brnd,'cat':cat,'subcat':subcat})

def manage_product(request):
    row = ''
    data = ''
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = product.objects.all()
        
    else:
        return redirect('/myadmin/signin')
    return render(request,'manage_product.html',{'row':row,'data':data})

def update_product(request,edit):
    row = ''
    data = ''
    brnd = ""
    cat = ""
    subcat = ""
    if 'admin_id' in request.session:
        row = sign_up.objects.filter(id=request.session['admin_id']).get()
        data = product.objects.filter(id=edit).get()
        brnd = brand.objects.all()
        cat = category.objects.all()
        subcat = sub_category.objects.all()
        if 'save' in request.POST:
            frm = PRODUCT(request.POST,request.FILES,instance=data)
            frm.save()
            return redirect("/myadmin/manage_product")
            
    else:
        return redirect('/myadmin/signin')
    return render(request,'add_product.html',{'row':row,'data':data,'brnd':brnd,'cat':cat,'subcat':subcat})

def delete_product(request,delt):
    data = product.objects.filter(id=delt).delete()
    return redirect('/myadmin/manage_product')