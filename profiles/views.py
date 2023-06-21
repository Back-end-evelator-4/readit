from django.shortcuts import render, redirect, reverse
from .models import Feedback
from blog.models import Blog


def about(request):
    feedbacks = Feedback.objects.order_by('-id')
    blogs = Blog.objects.order_by('-id')
    latest = blogs[:2]
    ctx = {
        'f_list': feedbacks,
    }
    return render(request, 'profiles/about.html', ctx)
