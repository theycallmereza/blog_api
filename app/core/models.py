from django.db import models


class Category(models.Model):
    """Category to be used for posts"""
    STATUS = {
        (0, 'Inactive'),
        (1, 'Active'),
    }
    name = models.CharField(max_length=255, unique=True)
    status = models.SmallIntegerField(default=1, choices=STATUS)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS = {
        (0, 'Inactive'),
        (1, 'Active'),
    }
    name = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=1, choices=STATUS)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = {
        (0, 'Inactive'),
        (1, 'Active'),
    }
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.SmallIntegerField(default=1, choices=STATUS)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts',
                                  blank=True)

    class Meta:
        ordering = ['-cdt']

    def __str__(self):
        return self.title
