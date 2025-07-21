from rest_framework import generics
from .models import Word
from .serializers import WordSerializer
import random

class WordList(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordOfTheDay(generics.RetrieveAPIView):
    serializer_class = WordSerializer

    def get_object(self):
        words = list(Word.objects.all())
        if not words:
            return None  # or raise Http404 if you want to return 404 when no words exist
        return random.choice(words)
