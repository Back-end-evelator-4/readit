from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category
from django.core.paginator import Paginator
from django.views import View


def home(request):
    blogs = Blog.objects.order_by('-id')
    latest = blogs[:2]
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        'blogs': page_obj,
    }
    return render(request, 'blog/index.html', ctx)


def blog_list(request):
    blogs = Blog.objects.order_by('-id')
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    if tag:
        blogs = blogs.filter(tags__title__exact=tag)
    cat = request.GET.get('category')
    if cat:
        blogs = blogs.filter(category__title__exact=cat)
    if q:
        blogs = blogs.filter(title__icontains=q)
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        'blogs': page_obj,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, **kwargs):
    resent_blog = Blog.objects.order_by('-id')[:3]
    obj = get_object_or_404(Blog, slug=kwargs['slug'], created_date__year=kwargs['year'],
                            created_date__month=kwargs['month'], created_date__day=kwargs['day'])
    obj.views += 1
    obj.save()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'resent_blog': resent_blog,
        'object': obj,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'blog/blog-single.html', ctx)
