from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm
from .models import CustomUser

# Create your views here.
@require_http_methods(['GET', 'POST'])
def base(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = LoginForm();
    else:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = f.get_user();
            auth_login(request, user)
            return redirect('home')
    return render(request, 'authentication/login.html', { 'form': f})

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f =SignupForm();
    else:
        f = SignupForm(request.POST)
        if f.is_valid():
            user = f.save();
            #send verification email as well.
            return render(request, 'authentication/signup_email_sent.html', { 'email' : user.email })
    return render(request, 'authentication/signup.html', { 'form': f})

@require_GET
def logout(request):
    auth_logout(request)
    return redirect('base');

@require_GET
@login_required
def home(request):
    return render(request, 'base/loggedin.html');

    
