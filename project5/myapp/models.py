from django.db import models

# Create your models here.
class django_abc(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    image = models.ImageField(upload_to='Images',null=True,blank=True)