from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood_score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    journal_entry = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s mood entry on {self.created_at}"

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    availability = models.JSONField()  # Store availability as JSON

    def __str__(self):
        return f"Therapist: {self.user.username}"

class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {'Anonymous' if self.is_anonymous else self.user.username}"