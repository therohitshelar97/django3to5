from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import  pre_save, pre_delete,post_save,post_delete
from django.dispatch import receiver
# Create your views here.
@receiver(pre_save, sender=User)
def before_save(sender,instance,*args,**kwargs):
    print("###################")
    print("before data save into the user")
    print("I Runnn")

@receiver(post_save,sender=User)
def after_save(sender,instance,created,*args,**kwargs):
    print("************")
    print("Data Save Succesfully........")

@receiver(pre_delete,sender=User)
def before_delete(sender,instance,*args,**kwargs):
    print("*****************")
    print("Before delete")

@receiver(post_delete,sender=User)
def after_delete(sender,instance,*args,**kwargs):
    print("***************")
    print("After delete")

@receiver(user_logged_in, sender=User)
def beginning(sender,request,user,**kwargs):
    print("Login Successfully.............")
    print("**********************")
    print("sender :",sender)
    print("request :",request)
    print("user :",user)
    print("kwrags:", kwargs)
    print("*********************")




