from rest_framework import viewsets
from rest_framework import filters

from core.models import Category, Post

from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        status = bool(
            int(self.request.query_params.get('status', 0))
        )
        queryset = self.queryset

        if status:
            queryset = queryset.filter(status=True)

        return queryset


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'category__name']
    ordering_fields = ['title', 'status', 'cdt', 'udt', 'category__name']

    def get_queryset(self):
        status = bool(
            int(self.request.query_params.get('status', 0))
        )
        queryset = self.queryset

        if status:
            queryset = queryset.filter(status=True)

        return queryset
