from django.contrib import admin
from .models import Profile, Feedback


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username', )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'feedback')
    fields = ('author', 'feedback')


