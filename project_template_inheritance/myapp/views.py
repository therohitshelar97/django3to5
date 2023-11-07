from django.shortcuts import render

# Create your views here.
def Base(request):
    return render(request, 'base.html')


def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Navbar(request):
    return render (request, 'navbar.html')