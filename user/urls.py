from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    # 회원가입
    path('register/', views.Signup.as_view(),name='register'),
    # 로그인
    path('login/', views.UserLogin.as_view(),name='login'),
    # 로그아웃
    path('logout/', views.UserLogout.as_view(),name='logout'),
    # 회원정보
    path('profile/', views.UserProfileDetail.as_view(),name='profile'),
    # 회원탈퇴
    path('withdrawal/', views.UserDrawal.as_view(),name='withdrawal'),
]