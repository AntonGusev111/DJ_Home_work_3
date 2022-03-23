from django.db import models
from django.utils.text import slugify

# id, name, price, image, release_date, lte_exists и slug

class Phone(models.Model):
    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

