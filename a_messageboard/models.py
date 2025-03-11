from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MessageBoard(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image=models.ImageField(upload_to='images', default='default.avif')
    subscribers = models.ManyToManyField(User, related_name="messageboard", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # First save to ensure we have an ID
        super().save(*args, **kwargs)
        
        # If name is not set, create default name
        if not self.name:
            self.name = f"Message board {self.id}"
            # Save again with the new name
            super().save(update_fields=['name'])

    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    messageboard=models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name="messages")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    body=models.TextField(max_length=200, null=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']
    def __str__(self):
        return str(self.author.username)