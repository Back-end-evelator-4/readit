from django.urls import path
from .views import about

app_name = 'profiles'


urlpatterns = [
    path('about/', about, name='about'),
]