from django.db import models

# Create your models here.

class Products(models.Model):
    pname = models.CharField(max_length=100, null=True)
    pprice = models.PositiveBigIntegerField(null=True)
    desc = models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.pname



