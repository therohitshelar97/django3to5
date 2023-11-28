from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Email(request):
    subject = "Welcome Bonus"
    message = 'Welcome To the It Vedant Institute'
    mail_from = settings.EMAIL_HOST_USER
    recipient_list = ['pranitdubal5@gmail.com','shubhamkhandangale625@gmail.com','chaitanya.gaikar143@gmail.com','manasishinde818@gmail.com']
    send_mail(subject,message,mail_from,recipient_list,fail_silently=False)
    return HttpResponse('mail send')


def SignUp(request):
    if request.method == "GET":
        username = request.GET.get('uname')
        first_name = request.GET.get('fname')
        last_name = request.GET.get('lname')
        email = request.GET.get('email')
        
        try:
            subject = f"Welcome {first_name} {last_name}"
            message = f"""
                        Dear {first_name} ,

                        Welcome to goa, have pleasant stay, hope you will enjoy
                        your holidays, 

                        Thank You For Selecting Us.

                        
                        Note:-
                        'Please Do Not Reply To This Mail, This is auto generated mail'

                    """
            mail_from = settings.EMAIL_HOST_USER
            recipient_list = [f"{email}"]
            send_mail(subject,message,mail_from,recipient_list)
            return render(request, 'signup.html')
        except:
            return render(request, 'signup.html')
