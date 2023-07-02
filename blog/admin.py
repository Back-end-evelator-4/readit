from django.contrib import admin
from .models import Tag, Category, Blog, SubBlog


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class SubBlogInlineAdmin(admin.StackedInline):
    model = SubBlog
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [SubBlogInlineAdmin]
    list_display = ('id', 'author', 'title', 'slug', 'category', 'created_date')
    fields = ('title', 'slug', 'author', 'image', 'description', 'tags', 'category', 'created_date', 'modifate_date')
    readonly_fields = ('created_date', 'modifate_date')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'author__user__username', 'category__title')
    filter_horizontal = ('tags',)
    list_editable = ('category', 'author')
    date_hierarchy = 'created_date'
    list_filter = ('created_date', 'tags', 'category')


@admin.register(SubBlog)
class SubBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog')
    fields = ('title', 'blog', 'image', 'description', 'content')
    list_editable = ('blog',)
