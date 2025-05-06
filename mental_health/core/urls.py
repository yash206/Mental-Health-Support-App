from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodEntryViewSet, TherapistViewSet, ForumPostViewSet

router = DefaultRouter()
router.register(r'mood-entries', MoodEntryViewSet)
router.register(r'therapists', TherapistViewSet)
router.register(r'forum-posts', ForumPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]