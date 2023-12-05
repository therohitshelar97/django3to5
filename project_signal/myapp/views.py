from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.signals import  pre_save, pre_delete,post_save,post_delete
from django.dispatch import receiver
# Create your views here.
@receiver(pre_save, sender=User)
def before_save(sender,instance,*args,**kwargs):
    print("###################")
    print("before data save into the user")
    print("I Runnn")




