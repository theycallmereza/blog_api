from rest_framework import viewsets
from rest_framework import filters
from rest_framework import pagination, generics
from rest_framework.decorators import action
from rest_framework import response
from django.shortcuts import get_object_or_404

from core.models import Category, Post, Tag

from .serializers import CategorySerializer, PostSerializer, TagSerializer


class PaginationClass(pagination.PageNumberPagination):
    page_size = 5


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        status = int(self.request.query_params.get('status', 0))
        queryset = self.queryset
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @action(methods=['GET'],
            detail=True,
            url_path='posts',
            url_name="posts", )
    def posts(self, request, pk=None):
        category = self.get_object()
        posts = category.post_set.all()
        serializer = PostSerializer(posts, many=True)
        return response.Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'category__name', 'tags__name']
    ordering_fields = ['title', 'status', 'cdt', 'udt', 'category__name']
    pagination_class = PaginationClass

    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        queryset = self.queryset
        if status is not None:
            int(status)
            queryset = queryset.filter(status=status)
        return queryset


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # @action(methods=['GET'],
    #         detail=True,
    #         url_path='posts',
    #         url_name="posts", )
    # def posts(self, request, pk=None):
    #     tag = self.get_object()
    #     posts = tag.posts.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return response.Response(serializer.data)


class PostsTagAPIVew(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PaginationClass

    def get_queryset(self):
        tag = get_object_or_404(Tag, id=self.kwargs['pk'])
        return tag.posts.all()
