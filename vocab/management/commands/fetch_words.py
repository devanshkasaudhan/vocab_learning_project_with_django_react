from django.core.management.base import BaseCommand
from vocab.models import Word
import requests
import time

class Command(BaseCommand):
    help = 'Fetch words from external API and populate database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of words to fetch (default: 10)',
        )
        parser.add_argument(
            '--level',
            type=str,
            choices=['Beginner', 'Intermediate', 'Advanced'],
            default='Intermediate',
            help='Difficulty level for the words',
        )

    def handle(self, *args, **options):
        count = options['count']
        level = options['level']
        
        self.stdout.write(f'Fetching {count} words at {level} level...')
        
        # Using WordsAPI (you'd need to sign up for an API key)
        # Alternative: use a word list file or other free APIs
        
        # For demonstration, here's a sample implementation using a word list
        word_lists = {
            'Beginner': [
                'happy', 'sad', 'big', 'small', 'fast', 'slow', 'good', 'bad', 
                'hot', 'cold', 'old', 'new', 'easy', 'hard', 'light', 'dark'
            ],
            'Intermediate': [
                'analyze', 'convince', 'emphasize', 'motivate', 'organize', 
                'prioritize', 'recognize', 'summarize', 'demonstrate', 'illustrate'
            ],
            'Advanced': [
                'quintessential', 'perspicacious', 'magnanimous', 'ineffable',
                'luminous', 'voracious', 'tenacious', 'sagacious', 'vivacious'
            ]
        }
        
        words_to_add = word_lists.get(level, word_lists['Intermediate'])[:count]
        
        created_count = 0
        for word_text in words_to_add:
            # You could integrate with dictionary APIs here
            # For now, using placeholder data
            word, created = Word.objects.get_or_create(
                word=word_text.capitalize(),
                defaults={
                    'definition': f'Definition for {word_text} (to be updated)',
                    'example': f'Example sentence using {word_text}.',
                    'level': level
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'Created: {word.word}')
                time.sleep(0.1)  # Rate limiting
            else:
                self.stdout.write(f'Already exists: {word.word}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {created_count} new words')
        )
