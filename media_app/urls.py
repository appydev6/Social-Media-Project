from django.urls import path
from . views import index_view, submit_post, like_post, profile_view, upload_profile_image, delete_post

urlpatterns = [
    path('', index_view, name='index'),
    path('submit-post/', submit_post, name='submit_post'),
    path('like-post/<int:post_id>/', like_post, name='like_post'),
    path('profile/<str:username>/', profile_view, name='profile_view'),
    path('upload-profile-image/', upload_profile_image, name='upload_profile_image'),
    path('delete-post/<int:post_id>/', delete_post, name='delete_post'),

]
