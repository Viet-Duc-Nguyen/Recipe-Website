from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #One to One if user is deleted, delete profile
    image = models.ImageField('default.jpg', upload_to = 'profile_pics', blank=True, null=True) #directory where images will be uploaded to, blank means no image will work

    def __str__(self):
        return f'{self.user.username} Profile'
    

# Signal to create a profile when a new user is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the profile when the user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()