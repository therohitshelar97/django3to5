from django.contrib import admin
from .models import django_abc

# Register your models here.
@admin.register(django_abc)
class AdminPanel(admin.ModelAdmin):
    display_list = ['name','age']