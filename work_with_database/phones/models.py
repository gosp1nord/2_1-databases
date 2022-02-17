from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=300)
    image = models.URLField()
    price = models.CharField(max_length=10)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=300, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)