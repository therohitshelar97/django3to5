from django.shortcuts import render, HttpResponseRedirect
from .models import django_abc,Cart
from .forms import abc_form

# Create your views here.

def Fetch(request):
    data = django_abc.objects.all()
    return render(request,'index.html',{'data':data})

def Form(request):
    if request.method == "POST":
        fm = abc_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
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
            return HttpResponseRedirect('/fetching/')
    else:
        pi = django_abc.objects.get(pk=id)
        fm = abc_form(instance=pi)
    return render(request,'update.html',{'form':fm})


def Animals(request):
    os = django_abc.objects.all()
    return render(request, 'animals.html',{'os':os})

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
    if request.method == "POST":
        cid = request.POST.get('cid')
        data = Cart.objects.create(django_abc_id=cid)
        data.save()
        return HttpResponseRedirect('/animals/')
    
def view_cart(request):
    cart_fetch = Cart.objects.all().values_list('django_abc_id', flat=True)
    cartitems = django_abc.objects.filter(id__in=cart_fetch)
    print(cart_fetch)
    return render(request,'viewcart.html', {'data':cartitems})