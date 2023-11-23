from django.shortcuts import render
from .models import Products

# Create your views here.

def Index(request):
    if request.method == "POST":
        search = request.POST.get('search')
        print(search)

        os = Products.objects.filter(pname__icontains=search)
    
    else:
        os = Products.objects.all()
    os1 = Products.objects.all()
      
   
    return render(request,'index.html',{'data':os, 'data1':os1})
