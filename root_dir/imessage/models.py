from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


class imessage (models.Model):    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    date = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=300)

    class Meta:
        verbose_name = ("Imessage")

    def __str__(self):
        return f'{self.reciever} Message'

    # def get_absolute_url(self):
    #     return reverse("imessage _detail", kwargs={"pk": self.pk})

