from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
import random

# Function to select a random default profile picture from the "static/Profiles" folder
def rand_profile():
    """Returns a random profile image from static/Profiles (only used at profile creation)."""
    profiles_path = os.path.join(settings.MEDIA_ROOT, 'Profiles')  # Use MEDIA_ROOT instead of STATICFILES_DIRS
    # Check if the folder exists and has files inside it
    if os.path.exists(profiles_path) and os.listdir(profiles_path):
        return '/Profiles/' + random.choice(os.listdir(profiles_path))  # Select a random image

    return 'images/avatar.svg'  # Fallback to a default image if the folder is empty or missing

# Profile model linked to Django's built-in User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relation with User model
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Profile picture (optional)
    displayname = models.CharField(max_length=20, null=True, blank=True)  # Display name (optional)
    info = models.TextField(null=True, blank=True)  # Additional profile information (optional)

    def __str__(self):
        return str(self.user)  # Display the username when referencing a Profile object

    @property
    def name(self):
        """Returns the display name if set; otherwise, uses the username."""
        return self.displayname if self.displayname else self.user.username 

    @property
    def avatar(self):
        """Returns the profile picture URL if set; otherwise, returns a default avatar."""
        if self.image:  # If a profile image exists, return its URL
            return self.image.url
        return f'{settings.STATIC_URL}{self.get_default_avatar()}'  # Return a random default avatar

    def get_default_avatar(self):
        """Caches and returns a random profile image only when the profile is first created."""
        if not hasattr(self, '_cached_avatar'):  # If no cached image, assign one
            self._cached_avatar = rand_profile()  # Assign a random profile image
        return self._cached_avatar  # Return the cached image path
        '''Ensures consistency – The profile image remains the same until explicitly changed.
✅ Reduces function calls – rand_profile() is only called once, improving performance.
✅ Prevents unnecessary database updates – The default image is stored once instead of recalculating it dynamically.'''

    def save(self, *args, **kwargs):
        """Assigns a random default image only when the profile is created."""
        if not self.image:  # Only set a default if no image was provided
            self.image = rand_profile()
        super().save(*args, **kwargs)  # Call the default save method to store changes
