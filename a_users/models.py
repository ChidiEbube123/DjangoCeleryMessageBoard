from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
import random
profile_images = [
    'Profiles/cs10000972928333981659.png',
    'Profiles/cs10029812482596167023.png',
    'Profiles/cs10036292168308093477.png',
    'Profiles/cs10041043183341837913.png',
    'Profiles/cs10044002801078706117.png',
    'Profiles/cs10052847777631991407.png',
    'Profiles/cs10053584490197742694.png',
    'Profiles/cs10059548803325392524.png',
    'Profiles/cs10062808705178013094.png',
    'Profiles/cs10074903523668009391.png',
    'Profiles/cs1007592202230585847.png',
    'Profiles/cs10080640731856853541.png',
    'Profiles/cs10096906769780188765.png',
    'Profiles/cs10101671332842947642.png',
    'Profiles/cs10107177797460378664.png',
    'Profiles/cs10109599096295916514.png',
    'Profiles/cs10121362914025265331.png',
    'Profiles/cs10126771986309177329.png',
    'Profiles/cs1014446996840049317.png',
    'Profiles/cs10149944615960090234.png',
    'Profiles/cs10157829562766181925.png',
    'Profiles/cs10160761440309538034.png',
    'Profiles/cs10162964341985417341.png',
    'Profiles/cs10164984782295999077.png',
    'Profiles/cs10177828363869959962.png',
    'Profiles/cs10188007868350593599.png',
    'Profiles/cs10191090027544985366.png',
    'Profiles/cs10199967553691032287.png',
    'Profiles/cs10205279313084001430.png',
    'Profiles/cs10220999042304702633.png',
    'Profiles/cs1023683139321898996.png',
    'Profiles/cs10244617136385016021.png',
    'Profiles/cs10249810206673574318.png',
    'Profiles/cs10258941429304026342.png',
    'Profiles/cs10260260226810328106.png',
    'Profiles/cs10271960416868893783.png',
    'Profiles/cs10274312235929497800.png',
    'Profiles/cs10278182741464528279.png',
    'Profiles/cs1028739694500438845.png',
    'Profiles/cs10304867809171149021.png',
    'Profiles/cs1031276169153944520.png',
    'Profiles/cs10317038593777694655.png',
    'Profiles/cs10319727602197422958.png',
    'Profiles/cs10320263970785138504.png',
    'Profiles/cs10332601358051050906.png',
    'Profiles/cs10344150597675026810.png',
    'Profiles/cs10347839973310989006.png',
    'Profiles/cs10351116564893241906.png',
    'Profiles/cs10358050775372481772.png',
    'Profiles/cs10363727687593091893.png',
    'Profiles/cs10367999321014852691.png',
    'Profiles/cs10375966263486909668.png',
    'Profiles/cs1038999582908600950.png',
    'Profiles/cs10395712722054270619.png',
    'Profiles/cs104029297788010187.png',
    'Profiles/cs10408841366876225671.png',
    'Profiles/cs1041658646643470663.png',
    'Profiles/cs10429043062607725946.png',
    'Profiles/cs1043313590853462920.png',
    'Profiles/cs10433537599246011514.png',
    'Profiles/cs10433873479498750733.png',
    'Profiles/cs10467585218834139847.png',
    'Profiles/cs10469288343204575838.png',
    'Profiles/cs10472946365052180966.png',
    'Profiles/cs10497074398658600598.png',
    'Profiles/cs10501922393764180689.png',
    'Profiles/cs10515268446512896392.png',
    'Profiles/cs10516410526411563735.png',
    'Profiles/cs1051701907529607458.png',
    'Profiles/cs10534208672672378193.png',
    'Profiles/cs10537024615327678295.png',
    'Profiles/cs10540246394928471665.png',
    'Profiles/cs10543170787319690934.png',
    'Profiles/cs1054853297164887286.png',
    'Profiles/cs10549232895008917502.png',
    'Profiles/cs10549437357841082133.png',
    'Profiles/cs10554074700371126251.png',
    'Profiles/cs10582659851228177470.png',
    'Profiles/cs10591762373777639709.png',
    'Profiles/cs10592796316240584115.png',
    'Profiles/cs1059414492272030008.png',
    'Profiles/cs10607004806280973918.png',
    'Profiles/cs10611814998591969063.png',
    'Profiles/cs10613747420647263699.png',
    'Profiles/cs10614911772227634956.png',
    'Profiles/cs10616525410493754688.png',
    'Profiles/cs10621633959661110015.png',
    'Profiles/cs10625613834389094323.png',
    'Profiles/cs10630622994341697087.png',
    'Profiles/cs10636637084375890929.png',
    'Profiles/cs106512632384455646.png',
    'Profiles/cs10666785984048987428.png',
    'Profiles/cs10668774279609500049.png',
    'Profiles/cs1067966361906104330.png',
    'Profiles/cs10685553598393197667.png',
    'Profiles/cs106882438988624722.png',
    'Profiles/cs10697859178343175771.png',
    'Profiles/cs1071100093264805170.png',
    'Profiles/cs10717079576109413948.png',
    'Profiles/cs10734390428580971257.png',
    'Profiles/cs10734422124108687056.png',
    'Profiles/cs10737225526842428256.png',
    'Profiles/cs10748819290670088511.png',
    'Profiles/cs1075474718017101696.png',
    'Profiles/cs10770772921357213798.png',
    'Profiles/cs10784541756976093719.png',
    'Profiles/cs10784896630897846255.png',
    'Profiles/cs10796678533607678181.png',
    'Profiles/cs10797378334060729297.png',
    'Profiles/cs10798038975385065098.png',
    'Profiles/cs10798960129453567574.png',
    'Profiles/cs10806659986020943337.png',
    'Profiles/cs10807180069531589624.png',
    'Profiles/cs10812994499431425475.png',
    'Profiles/cs10818353179956203450.png',
    'Profiles/cs10819950527080072980.png',
    'Profiles/cs10827289973197748462.png',
    'Profiles/cs10833096946207714466.png',
    'Profiles/cs10836565455201738925.png',
    'Profiles/cs10837049940242061383.png',
    'Profiles/cs10853784572025168728.png',
    'Profiles/cs1085635506802144513.png',
    'Profiles/cs10879781057885339687.png',
    'Profiles/cs10880518860203760618.png',
    'Profiles/cs10895037535915598795.png',
    'Profiles/cs10909575524567045113.png',
    'Profiles/cs10913623624498671090.png',
    'Profiles/cs10922443878724805553.png',
    'Profiles/cs10927036979269237573.png',
    'Profiles/cs10934824455494543852.png',
    'Profiles/cs10935977787421606691.png',
    'Profiles/cs10936474578844276197.png',
    'Profiles/cs10938497261139729603.png'
]

# Function to select a random default profile picture from the "static/Profiles" folder
def rand_profile():
    """Returns a random profile image from static/Profiles (only used at profile creation)."""
    profiles_path = os.path.join(settings.MEDIA_ROOT, 'Profiles')  # Use MEDIA_ROOT instead of STATICFILES_DIRS
    # Check if the folder exists and has files inside it
    if profile_images:
        return random.choice(profile_images)  # Select a random image

    return 'images/avatar.svg'  # Fallback to a default image if the folder is empty or missing

# Profile model linked to Django's built-in User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relation with User model
    image = models.ImageField(upload_to='avatars/',default='Profile/cs10935977787421606691.png', null=True, blank=True)  # Profile picture (optional)
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
        return f'{self.default_image_path}'

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
