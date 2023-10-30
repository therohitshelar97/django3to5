from django.shortcuts import render, HttpResponseRedirect
from .models import django_abc
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