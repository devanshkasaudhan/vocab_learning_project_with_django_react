# vocab/models.py
from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField(blank=True)
    level = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
