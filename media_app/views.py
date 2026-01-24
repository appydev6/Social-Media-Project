from django.shortcuts import render, redirect, get_object_or_404
from media_app.models import Post, LikePost, Profile
from user_auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count

def get_data(request, key):
    return request.GET.get(key) or request.POST.get(key)

# Create your views here.
@login_required(login_url='sign_in')
def index_view(request):
    user = request.user
    page_name = "index.html"
    data = {
        "already_liked_post_id": list(LikePost.objects.filter(user=user).values_list('post_id', flat=True)),
        "posts" : Post.objects.all().order_by('-created_at')
    }
    return render(request, page_name, context=data)

@login_required(login_url='sign_in')
def submit_post(request):
    user = request.user
    content = get_data(request, 'post_caption')
    image = request.FILES.get('post_image')
    Post.objects.create(
        user=user,
        caption=content,
        image=image,
    )
    return redirect('index')

@login_required(login_url='sign_in')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    LikePost.objects.get_or_create(user=request.user, post=post)
    user = request.user
    data = {
        "already_liked_post_id": list(LikePost.objects.filter(user=user).values_list('post_id', flat=True)),
        "posts": Post.objects.all().order_by('-created_at'),
    }
    return render(request, 'index.html', context=data)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('index')


@login_required(login_url='sign_in')
def profile_view(request, username):
    user = User.objects.get(username=username)
    page_name = "profile.html"
    data = {
        "top_posts": user.post.all().annotate(likes_received=Count("like_post")).order_by("-likes_received", "-created_at")[:3],
        'profile_user' : user,
        'posts_made' : user.post.count(),
                        # or Post.objects.filter(user=user).count(),
        'likes_made' : LikePost.objects.all().filter(user=user).count(),
                        # LikePost.objects.filter(user=user).count()
        'likes_recevied' : LikePost.objects.filter(post__user=user).count(), 
                            #post__user is  a lookup variable for reverse relationship.
    }
    return render(request, page_name, context=data)

@login_required(login_url='sign_in')
def upload_profile_image(request):
    user = request.user
    image = request.FILES['profile_image']    
    profile = Profile.objects.get(user=user)
    profile.image = image
    profile.save()
    return redirect(f'/profile/{user.username}')
