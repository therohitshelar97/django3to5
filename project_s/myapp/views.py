from django.shortcuts import render, HttpResponse,HttpResponseRedirect

# Create your views here.
def SetSessionData(request):
    request.session['first_name'] = 'Rohit'
    request.session['last_name'] = "Shelar"
    request.session.set_expiry(30)
    return HttpResponse('Session has been set')

def GetSessionData(request):
    try:
        fname = request.session['first_name']
        lname = request.session['last_name']
        return HttpResponse(f"My name is {fname} {lname}")
    except:
        return HttpResponse(f"Session has been Expired")
    
def Home(request):
    try:
        if request.session['first_name']:
            return render(request,'homepage.html')
    except:
        return HttpResponseRedirect('/setsession/')
