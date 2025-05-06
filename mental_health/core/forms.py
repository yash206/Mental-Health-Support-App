from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, MoodEntry


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class MoodEntryForm(forms.ModelForm):
    MOOD_CHOICES = [
        (1, '😢 Very Sad'),
        (2, '🙁 Sad'),
        (3, '😐 Neutral'),
        (4, '🙂 Happy'),
        (5, '😁 Very Happy'),
    ]

    mood_score = forms.ChoiceField(
        choices=MOOD_CHOICES,
        widget=forms.RadioSelect
    )
    journal_entry = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'How are you feeling today?'}),
        required=False
    )

    class Meta:
        model = MoodEntry
        fields = ['mood_score', 'journal_entry']