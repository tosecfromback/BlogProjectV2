from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    # 회원가입
    path('register/', views.SignupView.as_view(),name='register'),
    # 로그인
    path('login/', views.UserLoginView.as_view(),name='login'),
    # 로그아웃
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
    # 회원정보
    path('profile/', views.UserProfileDetailView.as_view(),name='profile'),
    # 회원탈퇴
    path('withdrawal/', views.UserDrawalView.as_view(),name='withdrawal'),
]