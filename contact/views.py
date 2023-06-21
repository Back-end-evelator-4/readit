from django.shortcuts import render, redirect, reverse
from .forms import ContactForm, Contact
from django.contrib import messages
from blog.models import Blog


def contact(request):
    blogs = Blog.objects.order_by('-id')
    latest = blogs[:2]
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'your request was accepted')
            return redirect('.')
    ctx = {
        'form': form,
    }
    return render(request, 'contact/contact.html', ctx)
