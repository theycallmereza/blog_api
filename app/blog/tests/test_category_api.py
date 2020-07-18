from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from core.models import Category, Post

from ..serializers import CategorySerializer, PostSerializer

CATEGORY_URL = reverse('blog:category-list')


class CategoryTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_category_list(self):
        """Test retrieving category list"""
        Category.objects.create(name='Category One')
        Category.objects.create(name='Category Two')

        response = self.client.get(CATEGORY_URL)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_category_successful(self):
        """Test create a new category"""
        payload = {'name': 'Category One'}
        self.client.post(CATEGORY_URL, payload)

        exists = Category.objects.filter(name=payload['name']).exists()

        self.assertTrue(exists)

    def test_create_category_invalid(self):
        """Test creating invalid category fails"""
        payload = {'name': ''}

        response = self.client.post(CATEGORY_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_category_exists(self):
        payload = {'name': 'Category One'}
        self.client.post(CATEGORY_URL, payload)

        response = self.client.post(CATEGORY_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_category_with_status_true(self):
        """Test filtering categories with status true"""
        category1 = Category.objects.create(name='Category One')
        category2 = Category.objects.create(name='Category Two', status=False)

        response = self.client.get(CATEGORY_URL, {'status': 1})

        serializer1 = CategorySerializer(category1)
        serializer2 = CategorySerializer(category2)

        self.assertNotIn(serializer2.data, response.data)
        self.assertIn(serializer1.data, response.data)

    def test_get_posts_related_to_category(self):
        """Test get posts related to a category"""
        category1 = Category.objects.create(name="Category One")
        category2 = Category.objects.create(name="Category Two")
        Post.objects.create(title="Post One", content="Some Text",
                            category=category1)
        Post.objects.create(title="Post Two", content="Some Text",
                            category=category2)

        url = reverse("blog:category-posts", args=[category1.id])

        response = self.client.get(url)

        serializer = PostSerializer(category1.post_set.all(), many=True)

        self.assertEqual(response.data, serializer.data)
