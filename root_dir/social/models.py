from django.db import models
from PIL import Image
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.contrib.humanize.templatetags import humanize


def validate_image(image):
    min_height = 590
    min_width = 590
    width, height = get_image_dimensions(image) 
    if width < min_width or height < min_height:
        raise ValidationError("Height or Width is lower than what is allowed")



class PostCreate(models.Model):
    user_name  = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField('image', upload_to="posts_pics", validators=[validate_image])
    date       = models.DateTimeField(default=timezone.now)
    likes      = models.ManyToManyField(User, blank=True, related_name="post_likes")

    class Meta:
        verbose_name_plural = ("Posts")

    def __str__(self):
        return f'{self.user_name} Post'

    def get_date(self):
        return humanize.naturaltime(self.date)

    def get_absolute_url(self):
        return reverse("social:home")
    
    def get_like_url(self):
        return reverse("social:Like-toggle")


    def save(self):
        super().save()
        img = Image.open(self.post_image.path)

        if img.height > 520 and img.width > 590:
            output_size = (590, 590)
            img.thumbnail(output_size)
            img.save(self.post_image.path)

class Bookmark(models.Model):
    bookmark = models.ForeignKey(PostCreate, on_delete=models.CASCADE, related_name='bookmarks')
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_bookmark')

    def __str__(self):
        return f'{self.user} Bookmark'
    

class Notifications(models.Model):
    post_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
    user_who_like = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostCreate, on_delete=models.CASCADE, related_name='post')
    date       = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = ("Notifications")

    def __str__(self):
        return f'{self.post_username} Notification'

    def get_date(self):
        return humanize.naturaltime(self.date)