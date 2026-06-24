from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets

#==============Post===========

# class PostListApi(ListAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostDetailApi(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#----------------viewset-------------------
# A viewset is a way to combine the logic for
# multiple related views into a single class

# instead PostListApi and PostDetailApi
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer


#==============User===========

# class UserListApi(ListAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetailApi(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

#----------------viewset-------------------
# A viewset is a way to combine the logic for
# multiple related views into a single class

# instead UserDetailApi and UserListApi
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset           = get_user_model().objects.all()
    serializer_class   = UserSerializer