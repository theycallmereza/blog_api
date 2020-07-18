from django.test import TestCase
from .. import models


class ModelTests(TestCase):

    def test_category_str(self):
        """Test the category string representation"""
        category = models.Category.objects.create(name='Test Category')

        self.assertEqual(str(category), category.name)

    def test_post_str(self):
        """Test the post string representation"""
        post = models.Post.objects.create(
            category=models.Category.objects.create(name="Test Category"),
            title="Test Title",
            content="Some Text"
        )

        self.assertEqual(str(post), post.title)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(name="Tag One")

        self.assertEqual(str(tag), tag.name)
