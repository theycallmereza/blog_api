from django.test import TestCase
from .. import models


class ModelTests(TestCase):

    def test_category_str(self):
        """Test the tag string representation"""
        category = models.Category.objects.create(name='Test Category')

        self.assertEqual(str(category), category.name)
