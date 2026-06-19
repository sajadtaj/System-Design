from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test', email='test@email.com', password='123Sec')

        cls.post = Post.objects.create(
            author=cls.user,
            title='A good title',
            body='Nice Body with amuzing content ',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice Body with amuzing content ')
        self.assertEqual(str(self.post),'A good title')