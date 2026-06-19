from django.urls import path, include
from .views import PostListApi, PostDetailApi

urlpatterns = [
    path("<int:pk>/",PostDetailApi.as_view(), name="post_detail"),
    path("",         PostListApi.as_view(),name="post_list"),
]
