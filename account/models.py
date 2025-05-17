from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user_to_follow):
        if not isinstance(user_to_follow, CustomUser):
             raise TypeError("Can only follow CustomUser instances.")
        if self != user_to_follow: # Prevent self-following
            self.following.add(user_to_follow)

    def unfollow(self, user_to_unfollow):
        if not isinstance(user_to_unfollow, CustomUser):
             raise TypeError("Can only unfollow CustomUser instances.")
        self.following.remove(user_to_unfollow)

    def is_following(self, user_to_check):
        if not isinstance(user_to_check, CustomUser):
             return False
        return self.following.filter(pk=user_to_check.pk).exists()

    def is_followed_by(self, user_to_check):
        if not isinstance(user_to_check, CustomUser):
             return False
        return self.followers.filter(pk=user_to_check.pk).exists()
