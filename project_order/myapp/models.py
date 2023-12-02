from django.db import models

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


