from django.db import models
from profiles.models import Profile
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True, unique_for_date='created_date', max_length=221)
    description = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateField(auto_now_add=True)
    modifate_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title

    @property
    def url_blog(self):
        return reverse('blog:detail', kwargs={
            'year': self.created_date.year,
            'month': self.created_date.month,
            'day': self.created_date.day,
            'slug': self.slug
        })


class SubBlog(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=221)
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
