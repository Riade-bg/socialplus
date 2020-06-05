from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)
    date_field = models.DateField()
    class Meta:
        verbose_name_plural = "Todo"
    def __str__(self):
        return self.text
    
    
