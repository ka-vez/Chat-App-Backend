from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to="user_images/", null=True, blank=True)
    verified = models.BooleanField(default=False)

    def save(self, *args,  **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


# create a user profile by default when user signs up
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()


#Automate the profile thing
post_save.connect(create_user_profile, sender=User)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:30]
    

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")

    message = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =  ['date']
        verbose_name_plural = "Message"

    def __str__(self):
        return f"{self.sender} - {self.receiver}"
    
    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile

    @property
    def receiver_profile(self):
        receiver_profile = Profile.objects.get(user=self.receiver)
        return receiver_profile