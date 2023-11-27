from django.db import models

# Create your models here.
class Product(models.Model):
    slug = models.SlugField(null=True, unique=True, default='')
    name = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.slug

