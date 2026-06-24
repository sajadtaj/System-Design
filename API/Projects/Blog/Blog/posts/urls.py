from django.urls import path, include
# from .views import PostListApi, PostDetailApi,UserDetailApi,UserListApi
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('',      PostViewSet, basename='posts')


# without ViewSet
# urlpatterns = [
    # path("<int:pk>/",      PostDetailApi.as_view(), name="post_detail"),
    # path("",               PostListApi.as_view(),   name="post_list"),
    # #---User
    # path("user/",          UserListApi.as_view(),   name="user_list"),
    # path("user/<int:pk>/", UserDetailApi.as_view(), name="user_detail"),
# ]

# With ViewSet
urlpatterns = router.urls
