from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, \
    IsAdminUser, \
    IsAuthenticatedOrReadOnly, \
    DjangoModelPermissionsOrAnonReadOnly, \
    SAFE_METHODS
from rest_framework import viewsets
from rest_framework.response import Response

class PostUserWritePermissions(BasePermission):
    message = "Editing post is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # check http if is in safe methods -> custom ermision
            return True

        return obj.author == request.user  # to do this request user must be loged in so request hase user field


#basic model viewset

class PostList(viewsets.ModelViewSet): # jeszcze bardziej abstrakcyjna klasa do zarządzania widokiem
    permission_classes = [PostUserWritePermissions]
    serializer_class = PostSerializer
    # queryset = Post.objects.all()

    def get_object(self, queryset=None, **kwargs): #kwargs arqumenty http requestu
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # Define Custom Query set
    def get_queryset(self):
        return Post.objects.all()


# basic view set
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all() # Kluczowy elememt viewSet
#
#     # Zwracanie listy postow
#     def list(self, request): # to samo co PostList widok
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass


# Old we will recreate then in viesets
# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]  # Define model permision behavioru
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermissions):
#     permission_classes = [PostUserWritePermissions]  # Use custom permision created above
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


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
