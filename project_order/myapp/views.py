from django.shortcuts import render, HttpResponseRedirect
from .models import Products, Cart, Order, Address
from .forms import AddressForm

# Create your views here.

def Product1(request):
    os = Products.objects.all()
    return render(request,'products.html', {'data':os})

def Cart1(request):
    return render(request,'cart.html')

def order_place(request):
    if request.method == "POST":
        os = Address.objects.all().values_list('id',flat=True)
        product = request.POST.get('pid')
        Order.objects.create(product_id=product,address_id=os)
        return HttpResponseRedirect('/address/')

def Order1(request):
    return render(request,'orders.html')

def view_order(request):
    order = Order.objects.all().values_list('product_id', flat=True)
    order1 = Order.objects.all().values_list('address_id', flat=True)
    products = Products.objects.filter(id__in=order)
    address = Address.objects.filter(id__in=order1)

    return render(request,'view_order.html', {'product':products,'address':address})

def addAddress(request):
    if request.method == "POST":
        fm = AddressForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = AddressForm()
            return HttpResponseRedirect('/order/')
    else:
        fm = AddressForm()
    os = Address.objects.all()
    return render(request,'address.html',{'form':fm,'addr':os})

