from django.urls import path
from .views import WordList, WordOfTheDay

urlpatterns = [
    path('words/', WordList.as_view(), name='word-list'),
    path('word-of-the-day/', WordOfTheDay.as_view(), name='word-of-the-day'),
]
