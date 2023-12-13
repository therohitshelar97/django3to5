from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import django_abc,Cart
from .forms import abc_form, SignUp_Form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def Fetch(request):
    
    try:
        data = django_abc.objects.all()
        # messages.success(request,"Data Enter SuccessFully")
        return render(request,'index.html',{'data':data})
    except:
        messages.success(request,"Something went Wrong")
        return render(request,'index.html')


def Form(request):
    if request.method == "POST":
        fm = abc_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Enter Succesfully")
            return HttpResponseRedirect('/fetching/')
    else:
        fm = abc_form()
    return render(request,'forms.html',{'form':fm})

def Update(request,id):
    if request.method == "POST":
        pi = django_abc.objects.get(pk=id)
        fm = abc_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Updated Successfully")
            return HttpResponseRedirect('/fetching/')
    else:
        pi = django_abc.objects.get(pk=id)
        fm = abc_form(instance=pi)
    return render(request,'update.html',{'form':fm})
# def Delete(request,id):
#     if request.method == "post":
#         os


def Animals(request):
    if request.user.is_authenticated:
        os = django_abc.objects.all()
        cart_fetch = Cart.objects.filter(user=request.user).values_list('django_abc_id', flat=True)
        cartitems = django_abc.objects.filter(id__in=cart_fetch)
        count = cartitems.count()
        print(request.user)
    
        # dd = django_abc.objects.all().values_list('id',flat=True)
        # f = django_abc.objects.filter(id__in=dd)
        # f.delete()

        return render(request, 'animals.html',{'os':os, 'count':count})
    else:
        return HttpResponseRedirect('/login/')

def Static1(request):
    return render (request, 'static_image.html')


def Orm(request):
    # data = django_abc.objects.all() #fetching all data from table its like select * from table in mysql
    # data = django_abc.objects.all().values_list('id',flat=True) #here we are selecting all ids from table its like select id from tablename in django
    # data = django_abc.objects.all()[:2]  #selecting top 2 records its working like limit keyword
    # data = django_abc.objects.get(pk=4) # 
    # data = django_abc.objects.get(id=1)
    # data = django_abc.objects.filter(name='tom')
    # data = django_abc.objects.filter(name__startswith='M')
    # data = django_abc.objects.filter(name__istartswith='H').filter(name__iendswith='e')
    # data = django_abc.objects.filter(name__contains='bhai')
    # data = django_abc.objects.filter(name__icontains='some')
    # data = django_abc.objects.filter(name__exact='Tom')
    # data = django_abc.objects.exclude(id__in=[1,3,5])
    # data = django_abc.objects.filter(id=4).update(name='Tom Cruise')
    # data = django_abc.objects.filter(id__in=[5,7,8,9]).update(name='Handsome Dogs')
    # data = django_abc.objects.get(id=10).delete()
    # data = django_abc.objects.create(name='Ameya',age=9,image='Images/dog.jpg' )
    # data = django_abc.objects.filter(age__gte=11)
    # data = django_abc.objects.filter(age__lte=11)
    # data = django_abc.objects.count()
    data = django_abc.objects.aggregate(max('age',default=0))

    return render(request,'orm.html',{'data':data})

def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cid = request.POST.get('cid')
            item,data = Cart.objects.get_or_create(django_abc_id=cid,user=request.user)
            print(item, data)

            if not data:
                item.quantity+=1
                item.save()
            return HttpResponseRedirect('/animals/')
    
def cart_increse(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            item,data = Cart.objects.get_or_create(django_abc_id=cid)
            print(item, data)

            if not data:
                item.quantity+=1
                item.save()
            return HttpResponseRedirect('/viewcart/')
    
def cart_decrese(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            item,data = Cart.objects.get_or_create(django_abc_id=cid)
            print(item, data)

            if not data:
                item.quantity-=1
                item.save()
                if item.quantity<1:
                    item.delete()

            return HttpResponseRedirect('/viewcart/')

    
def view_cart(request):
    if request.user.is_authenticated:
        cart_fetch = Cart.objects.filter(user_id=request.user).values_list('django_abc_id',flat=True)
        print(cart_fetch)
        # cart_fetch = Cart.objects.all().values_list('django_abc_id', flat=True)
        cartitems = django_abc.objects.filter(id__in=cart_fetch)
        username = request.user
        # count = cartitems.count()

        # allq = Cart.objects.all()
        # print(cart_fetch)
        return render(request,'viewcart.html', {'data':cartitems,'user':username})
    else:
        return HttpResponseRedirect('/login/')

def remove_cart(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            os = Cart.objects.filter(django_abc_id=id)
            print(os)
            os.delete()
            print(id)
            return HttpResponseRedirect('/viewcart/')
    
def SignUp(request):
    if request.method == "POST":
        fm = SignUp_Form(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUp_Form()
    return render(request,'signup.html', {'form':SignUp_Form})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/animals/')
    
    return render(request, 'login.html')


def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')