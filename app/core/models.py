from django.db import models


class Category(models.Model):
    """Category to be used for posts"""
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
