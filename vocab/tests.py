from django.test import TestCase, Client
from django.urls import reverse
from vocab.models import Word
from rest_framework import status

class WordModelTest(TestCase):
    def setUp(self):
        self.word = Word.objects.create(
            word="Test",
            definition="A test definition",
            example="This is a test example",
            level="Beginner"
        )

    def test_word_creation(self):
        """Test that word is created properly"""
        self.assertEqual(self.word.word, "Test")
        self.assertEqual(self.word.definition, "A test definition")
        self.assertEqual(self.word.level, "Beginner")
        self.assertEqual(str(self.word), "Test")

    def test_word_levels(self):
        """Test word level choices"""
        levels = ['Beginner', 'Intermediate', 'Advanced']
        for level in levels:
            word = Word.objects.create(
                word=f"Test{level}",
                definition=f"Test definition for {level}",
                level=level
            )
            self.assertEqual(word.level, level)

class WordAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.word = Word.objects.create(
            word="API Test",
            definition="A test definition for API",
            example="This is an API test example",
            level="Intermediate"
        )

    def test_word_list_api(self):
        """Test word list API endpoint"""
        url = reverse('word-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "API Test")

    def test_word_of_the_day_api(self):
        """Test word of the day API endpoint"""
        url = reverse('word-of-the-day')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if response contains expected fields
        data = response.json()
        self.assertIn('word', data)
        self.assertIn('definition', data)
        self.assertIn('level', data)

    def test_word_of_the_day_empty_database(self):
        """Test word of the day API when no words exist"""
        Word.objects.all().delete()
        url = reverse('word-of-the-day')
        response = self.client.get(url)
        # Should handle gracefully when no words exist
        self.assertIn(response.status_code, [status.HTTP_404_NOT_FOUND, status.HTTP_200_OK])
