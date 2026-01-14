from django.shortcuts import render, redirect
from media_app.models import Post

def get_data(request, key):
    return request.GET.get(key) or request.POST.get(key)

# Create your views here.
def index_view(request):
    page_name = "index.html"
    return render(request, page_name)

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