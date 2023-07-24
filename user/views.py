from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from .forms import RegisterForm, LoginForm


# Create your views here.

### Join
class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')



### LogIn
class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            # email = form.cleaned_data['username']
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('blog:list')
            
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)

### LogOut
class UserLogout(View):
    def post(self, request):
        logout(request)
        redirect('index.html')
        return render(request, 'base.html')

### Profile
class UserProfileDetail(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class UserProfileUpdate(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class UserDrawal(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

