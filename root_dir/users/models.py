from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="default.jpg", upload_to="profile_pics")
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path).convert('RGB')
        if img.width > 500 or img.height > 500:
            img.thumbnail((500, 500))

        if img.height < img.width:
            left = (img.width - img.height) / 2
            right = (img.width + img.height) / 2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))

        elif img.width < img.height:
            left = 0
            right = img.width
            top = 0
            bottom = img.width
            img = img.crop((left, top, right, bottom))

        img.save(self.avatar.path)