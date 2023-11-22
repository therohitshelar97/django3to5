from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class django_abc(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    price = models.IntegerField(null=True)
    des = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='Images',null=True,blank=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    django_abc = models.ForeignKey(django_abc, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True)