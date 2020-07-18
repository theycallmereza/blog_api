from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('posts', views.PostViewSet)
router.register('tags', views.TagViewSet)

app_name = 'blog'

urlpatterns = [
    path('', include(router.urls)),
]
