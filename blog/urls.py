from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록
    path("", views.PostListView.as_view(), name='list'),
    # 글 작성
    path("write/", views.PostCreateView.as_view(), name='write'),
    # 글 상세
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 글 수정
    path("detail/<int:pk>/edit/", views.PostUpdateView.as_view(), name='edit'),
    # 글 삭제
    path("detail/<int:pk>/delete/", views.PostDeleteView.as_view(), name='delete'),
    # 글 검색
    path("search/<str:tag>/", views.PostSearchView.as_view(), name="search"),

    # 댓글 작성
    path("detail/<int:pk>/", views.CommentCreateView.as_view(), name="cm_write"),
    # 댓글 수정
    path("detail/<int:pk>/", views.CommentUpdateView.as_view(), name="cm_edit"),
    # 댓글 삭제
    path("detail/<int:pk>/", views.CommentDeleteView.as_view(), name="cm_delete"),

    # 대댓글 작성
    path("detail/<int:pk>/", views.ReCommentCreateView.as_view(), name="re_write"),
    # 대댓글 수정
    path("detail/<int:pk>/", views.ReCommentUpdateView.as_view(), name="re_edit"),
    # 대댓글 삭제
    path("detail/<int:pk>/", views.ReCommentDeleteView.as_view(), name="re_delete"),

]