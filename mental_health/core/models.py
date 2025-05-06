from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_therapist = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

class MoodEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mood_score = models.IntegerField()
    journal_entry = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Mood Score: {self.mood_score}"

class TherapistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    availability = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Therapist: {self.user.username}"

class ForumPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {'Anonymous' if self.is_anonymous else self.user.username}"
