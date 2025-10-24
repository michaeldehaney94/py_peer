from django.db import models
from django.contrib.auth import get_user_model

# User Model
User = get_user_model() # use the django built-in user model database

# Profile Model.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # act as the foreign key
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='test-profile.png')
    location = models.CharField(max_length=100, blank=True)


# returns the username as a preview
def __str__(self):
    return self.user.username



