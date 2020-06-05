from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural = "Search"
    def __str__(self):
        return self.search

    # def get_absolute_url(self):
    #     return reverse("craiglist:Search", kwargs={"pk": self.pk})
