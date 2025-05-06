from rest_framework import serializers
from .models import MoodEntry, Therapist, ForumPost
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ['id', 'mood_score', 'journal_entry', 'created_at']

class TherapistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Therapist
        fields = ['id', 'user', 'specialization', 'license_number', 'availability']

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id', 'content', 'is_anonymous', 'created_at']