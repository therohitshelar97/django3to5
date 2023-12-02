from django.shortcuts import render, HttpResponseRedirect
from .models import Products, Cart, Order

# Create your views here.

def Product1(request):
    os = Products.objects.all()
    return render(request,'products.html', {'data':os})

def Cart1(request):
    return render(request,'cart.html')

def order_place(request):
    if request.method == "POST":
        product = request.POST.get('pid')
        Order.objects.create(product_id=product)
        return HttpResponseRedirect('/order/')

def Order1(request):
    return render(request,'orders.html')

def view_order(request):
    order = Order.objects.all().values_list('product_id', flat=True)
    products = Products.objects.filter(id__in=order)
    return render(request,'view_order.html', {'product':products})
