from rest_framework import viewsets
from rest_framework import filters
from rest_framework import pagination
from rest_framework.decorators import action
from rest_framework import response

from core.models import Category, Post

from .serializers import CategorySerializer, PostSerializer


class PaginationClass(pagination.PageNumberPagination):
    page_size = 5


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

    @action(methods=['GET'], detail=True, url_path='posts',
            url_name="posts")
    def posts(self, request, pk=None):
        category = self.get_object()
        posts = category.post_set.all()
        serializer = PostSerializer(posts, many=True)
        return response.Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'category__name']
    ordering_fields = ['title', 'status', 'cdt', 'udt', 'category__name']
    pagination_class = PaginationClass

    def get_queryset(self):
        status = bool(
            int(self.request.query_params.get('status', 0))
        )
        queryset = self.queryset

        if status:
            queryset = queryset.filter(status=True)

        return queryset
