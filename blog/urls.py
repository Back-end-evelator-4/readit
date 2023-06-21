from django.urls import path
from .views import home, blog_list, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog_list, name='list'),
    path('blog/detail/<str:year>/<str:month>/<str:day>/<slug:slug>/', blog_detail, name='detail'),
]
