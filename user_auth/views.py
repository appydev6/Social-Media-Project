from django.shortcuts import render

# Create your views here.
def sign_up_view(request):
    page_name = 'sign_up.html'
    if request.method == "GET":
        return render(request, page_name)
    else: # POST
        pass

def sign_in_view(request):
    pass

def sign_out_view(request):
    pass
