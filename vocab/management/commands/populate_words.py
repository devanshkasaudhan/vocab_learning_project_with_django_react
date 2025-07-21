from django.core.management.base import BaseCommand
from vocab.models import Word
import json

class Command(BaseCommand):
    help = 'Populate the database with sample vocabulary words'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='JSON file path containing words data',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing words before adding new ones',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Word.objects.all().delete()
            self.stdout.write(self.style.WARNING('Cleared all existing words'))

        # Sample vocabulary words
        sample_words = [
            {
                "word": "Serendipity",
                "definition": "The occurrence and development of events by chance in a happy or beneficial way",
                "example": "A fortunate stroke of serendipity led her to discover the hidden talent.",
                "level": "Advanced"
            },
            {
                "word": "Eloquent",
                "definition": "Fluent or persuasive in speaking or writing",
                "example": "The speaker delivered an eloquent speech that moved the audience to tears.",
                "level": "Intermediate"
            },
            {
                "word": "Ubiquitous",
                "definition": "Present, appearing, or found everywhere",
                "example": "Smartphones have become ubiquitous in modern society.",
                "level": "Advanced"
            },
            {
                "word": "Resilient",
                "definition": "Able to withstand or recover quickly from difficult conditions",
                "example": "The community proved resilient after the natural disaster.",
                "level": "Intermediate"
            },
            {
                "word": "Ephemeral",
                "definition": "Lasting for a very short time",
                "example": "The beauty of cherry blossoms is ephemeral, lasting only a few weeks.",
                "level": "Advanced"
            },
            {
                "word": "Curious",
                "definition": "Eager to know or learn something",
                "example": "She was curious about how the machine worked.",
                "level": "Beginner"
            },
            {
                "word": "Brave",
                "definition": "Ready to face and endure danger or pain; showing courage",
                "example": "The brave firefighter rescued the cat from the tree.",
                "level": "Beginner"
            },
            {
                "word": "Benevolent",
                "definition": "Well meaning and kindly",
                "example": "The benevolent king was loved by all his subjects.",
                "level": "Intermediate"
            },
            {
                "word": "Pragmatic",
                "definition": "Dealing with things sensibly and realistically",
                "example": "She took a pragmatic approach to solving the budget crisis.",
                "level": "Intermediate"
            },
            {
                "word": "Mellifluous",
                "definition": "Sweet or musical; pleasant to hear",
                "example": "The singer's mellifluous voice captivated the audience.",
                "level": "Advanced"
            }
        ]

        # If file is provided, load from file
        if options['file']:
            try:
                with open(options['file'], 'r') as f:
                    words_data = json.load(f)
            except FileNotFoundError:
                self.stdout.write(self.style.ERROR(f'File {options["file"]} not found'))
                return
            except json.JSONDecodeError:
                self.stdout.write(self.style.ERROR('Invalid JSON file'))
                return
        else:
            words_data = sample_words

        # Create words
        created_count = 0
        for word_data in words_data:
            word, created = Word.objects.get_or_create(
                word=word_data['word'],
                defaults={
                    'definition': word_data['definition'],
                    'example': word_data.get('example', ''),
                    'level': word_data['level']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created: {word.word}')
            else:
                self.stdout.write(f'Already exists: {word.word}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {created_count} new words')
        )
