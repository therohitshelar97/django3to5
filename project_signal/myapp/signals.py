from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out, user_login_failed
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def beginning(sender,request,user,**kwargs):
    print("Login Successfully.............")
    print("**********************")
    print("sender :",sender)
    print("request :",request)
    print("user :",user)
    print("kwrags:", kwargs)
    print("*********************")

# user_logged_in.connect(beginning, sender=User)

@receiver(user_logged_out, sender=User)
def the_end(sender,request,user,**kwargs):
    print("**********************")
    print("LogOut Signals")

@receiver(user_login_failed)
def error(sender, credentials,**kwargs):
    print("*********************")
    print("User Login failed")