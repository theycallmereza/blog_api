from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag, Post, Category

from ..serializers import TagSerializer, PostSerializer

TAGS_URL = reverse('blog:tag-list')


class TagTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(name='Tag One')
        Tag.objects.create(name='Tag Two')

        response = self.client.get(TAGS_URL)

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_tag_successful(self):
        """Test creating new tag"""
        payload = {'name': 'Test Tag'}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(
            name=payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating new tag with invalid payload"""
        payload = {'name': ''}
        response = self.client.post(TAGS_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_posts_by_tag(self):
        """Test filtering posts with tag"""
        tag1 = Tag.objects.create(name="Tag One")
        Tag.objects.create(name="Tag Two")
        category = Category.objects.create(name="Category")
        post1 = Post.objects.create(title="Title",
                                    content="Content",
                                    category=category)
        post1.tags.add(tag1)
        Post.objects.create(title="Title",
                            content="Content",
                            category=category)
        url = reverse('blog:posts-tag', args=[tag1.id])
        response = self.client.get(url)

        serializer = PostSerializer(tag1.posts.all(), many=True)

        self.assertEqual(response.data['results'], serializer.data)
