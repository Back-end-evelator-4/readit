from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles', null=True, blank=True)
    position = models.CharField(null=True, blank=True, max_length=221)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        full_name = []
        if self.user.first_name:
            full_name.append(self.user.first_name)
        if self.user.last_name:
            full_name.append(self.user.last_name)
        if full_name:
            return " ".join(full_name)
        return self.user.username


class Feedback(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"{self.author}'feedback"


def profile_post_save(instance, sender, created, *args, **kwargs):
    if created:
        obj = Profile.objects.create(user=instance)
        return obj
    return None


post_save.connect(profile_post_save, sender=User)
