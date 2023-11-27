from django.shortcuts import render
from .models import Products
from django.db.models import Q

# Create your views here.

def Index(request):
    if request.method == "POST":
        search = request.POST.get('search')
        print(search)

        os = Products.objects.filter(Q(pname__icontains=search)| Q(pprice__icontains=search) | Q(desc__icontains=search)|Q(category__icontains=search))
    
    else:
        os = Products.objects.all()
    os1 = Products.objects.all()
      
   
    return render(request,'index.html',{'data':os, 'data1':os1})
