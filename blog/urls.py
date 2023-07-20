from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록
    path("", views.PostList.as_view(), name='list'),
    # 글 작성
    path("write/", views.PostCreate.as_view(), name='write'),
    # 글 상세
    path("detail/<int:pk>/", views.PostDetail.as_view(), name='detail'),
    # 글 수정
    path("detail/<int:pk>/edit/", views.PostUpdate.as_view(), name='edit'),
    # 글 삭제
    path("detail/<int:pk>/delete/", views.PostDelete.as_view(), name='delete'),
    # 글 검색
    path("search/<str:tag>/", views.PostSearch.as_view(), name="search"),

    # 댓글 작성
    path("detail/<int:pk>/", views.CommentCreate.as_view(), name="cm-write"),
    # 댓글 수정
    path("detail/<int:pk>/", views.CommentUpdate.as_view(), name="cm-edit"),
    # 댓글 삭제
    path("detail/<int:pk>/", views.CommentDelete.as_view(), name="cm-delete"),

    # # 대댓글 작성
    # path("detail/<int:pk>/", views.ReCommentCreate.as_view(), name="re_write"),
    # # 대댓글 수정
    # path("detail/<int:pk>/", views.ReCommentUpdate.as_view(), name="re_edit"),
    # # 대댓글 삭제
    # path("detail/<int:pk>/", views.ReCommentDelete.as_view(), name="re_delete"),

]