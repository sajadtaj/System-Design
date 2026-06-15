from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from books.models import Book


class ApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Book 1",
            subtitle="Book 1",
            author="Author",
            isbn=1234567,
        )

    def test_api_list(self):
        response = self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
