from django.shortcuts import render

# Create your views here.
def index_view(request):
    page_name = "index.html"
    return render(request, page_name)