from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    feature     = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("website:Product", kwargs={"id": self.id})