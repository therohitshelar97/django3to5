from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Email(request):
    subject = "Welcome Bonus"
    message = 'Welcome To the It Vedant Institute'
    mail_from = settings.EMAIL_HOST_USER
    recipient_list = ['pranitdubal5@gmail.com',]
    send_mail(subject,message,mail_from,recipient_list,fail_silently=False)
    return HttpResponse('mail send')



