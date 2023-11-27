from django.shortcuts import render
from .models import Product

# Create your views here.
def Index(request):
    os = Product.objects.all()
    return render(request,'index.html',{'data':os})


def DS(request,slug):
    os = Product.objects.filter(slug=slug).values()
    return render(request,'courses.html',{'os':os})
