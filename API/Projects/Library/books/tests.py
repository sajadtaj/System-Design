from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title     = 'Test Book',
            subtitle = 'Test Sub Book',
            author    = 'Test Author',
            isbn      = 123456789,
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.subtitle, 'Test Sub Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, 123456789)

    def test_book_listview(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200),
        self.assertContains(response, 'Test Book')
        self.assertContains(response, 'Test Sub Book')
        self.assertTemplateUsed(response,"books/book_list.html")
