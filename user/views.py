from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
# from .forms import RegisterFrom

# Create your views here.

### Join
class SignupView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### LogIn
class UserLoginView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### LogOut
class UserLogoutView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### Profile
class UserProfileDetailView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class UserProfileUpdateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class UserDrawalView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

