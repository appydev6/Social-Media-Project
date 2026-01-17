from django.shortcuts import render, redirect, get_object_or_404
from media_app.models import Post, LikePost
from django.contrib.auth.decorators import login_required

def get_data(request, key):
    return request.GET.get(key) or request.POST.get(key)

# Create your views here.
def index_view(request):
    page_name = "index.html"
    data = {
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
    return redirect('index')