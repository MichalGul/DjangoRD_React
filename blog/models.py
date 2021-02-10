from django.db import models
from django.contrib.auth.models import User  # django user model
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # return only published posts, custom models manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ('draft', "Draft"),
        ('published', "Published")
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 default=1)  # models protect-> delete post dont delete category
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='published')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager to filter
    postobjects = PostObjects()  # our custom manager

    class Meta:  # tutaj mozna dodac wszystko co nie jest polem, opce order, nazwe tabeli w bazie etc. https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options
        ordering = ('-published',)

    def __str__(self):
        return self.title
