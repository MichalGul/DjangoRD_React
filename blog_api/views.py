from django.shortcuts import render
from rest_framework import generics, status
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, \
    IsAdminUser, \
    IsAuthenticatedOrReadOnly, \
    DjangoModelPermissionsOrAnonReadOnly, \
    SAFE_METHODS


class PostUserWritePermissions(BasePermission):
    message = "Editing post is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # check http if is in safe methods -> custom ermision
            return True

        return obj.author == request.user  # to do this request user must be loged in so request hase user field


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Define model permision behavioru
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermissions):
    permission_classes = [PostUserWritePermissions]  # Use custom permision created above

    queryset = Post.objects.all()
    serializer_class = PostSerializer


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
