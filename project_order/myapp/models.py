from django.db import models
from django.utils import timezone
import datetime
import uuid

# Create your models here.
class Products(models.Model):
    pname = models.CharField(max_length=100, null=True)
    price = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return self.pname

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)


class Address(models.Model):
    address = models.CharField(max_length=1000, null=True)
    city = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    landmark = models.CharField(max_length=200,null=True)

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True)
    order_id = models.CharField(max_length=100, null=True, unique=True)

    def save(self,*args,**kwargs):
        if not self.order_id:
            # current_time = timezone.now()
            print(datetime.datetime.now())
            current_time = datetime.datetime.now()
            order_id = f'{current_time.strftime("%Y%d%m%H%M%S")}-{uuid.uuid4().hex[:6]}'
            self.order_id = order_id
        super().save(*args, **kwargs)







