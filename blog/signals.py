from .models import Blog
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    return instance


pre_save.connect(blog_pre_save, sender=Blog)

