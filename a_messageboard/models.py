
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
import random
from django.core.cache import cache

def rand_messageboard_image():
    """Returns a random image from static/messageboard_images (used only at creation)."""
    images_path = os.path.join(settings.BASE_DIR, 'static/DP')
    if os.path.exists(images_path) and os.listdir(images_path):
        return 'DP/' + random.choice(os.listdir(images_path))
    return 'images/default.avif'  # Fallback default image

class MessageBoard(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)  
    subscribers = models.ManyToManyField(User, related_name="messageboard", blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        """Ensures a default image is assigned only once at creation."""
        if not self.id:  # New instance (not yet saved to DB)
            self.image = self.get_default_image()
        
        super().save(*args, **kwargs)  # Save to DB

        # If name is not set, create a default name
        if not self.name:
            self.name = f"Message board {self.id}"
            super().save(update_fields=['name'])

    def get_default_image(self):
        """Caches and returns a random image only when the message board is first created."""
        if not hasattr(self, '_cached_image'):
            self._cached_image = rand_messageboard_image()  # Assign a random image
        return self._cached_image  # Return the cached image

    
class Message(models.Model):
    messageboard=models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name="messages")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    body=models.TextField(max_length=200, null=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']
    def __str__(self):
        return str(self.author.username)