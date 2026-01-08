from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from user_auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from media_app.models import Profile

# Create your views here.
def sign_up_view(request):
    page_name = 'sign_up.html'
    if request.method == "GET":
        return render(request, page_name)
    else: # POST
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if not email:
            return render(request, page_name, context={'error': True, 'error_msg': 'Email is required'})
        if not username:
            return render(request, page_name, context={'error': True, 'error_msg': 'Username is required'})
        if not password:
            return render(request, page_name, context={'error': True, 'error_msg': 'Password is required'})
        if User.objects.filter(email=email).exists():
            return render(request, page_name, context={'error': True, 'error_msg': 'Email already in use'})
        if User.objects.filter(username=username).exists():
            return render(request, page_name, context={'error': True, 'error_msg': 'Username already in use'})
        User.objects.create_user(email=email, username=username, password=password)
        user = auth.authenticate(username=username, password=password)
        Profile.objects.get_or_create(user=user)
        auth.login(request, user)
        return render(request, page_name)

def sign_in_view(request):
    page_name = 'sign_in.html'
    if request.method == "GET":
        return render(request, page_name)
    else: # POST
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if not user:
            return render(request, page_name, context={'error': True, 'error_msg': 'Invalid credentials'})
        Profile.objects.get_or_create(user=user)
        auth.login(request, user)
        return render(request, page_name)

@login_required
def delete_user_view(request):
    # print(f"User authenticated: {request.user.is_authenticated}")  # Add this
    # print(f"Method: {request.method}")
    
    page_name = 'sign_up.html'
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        context = {
            "message": "User deleted successfully."
        }
        return render(request, page_name, context)
    return render(request, page_name)
    
def sign_out_view(request):
    auth.logout(request)
    return redirect('sign_in')
