from django.urls import path
from . views import index_view, submit_post

urlpatterns = [
    path('', index_view, name='index'),
    path('submit-post/', submit_post, name='submit_post'),
]
