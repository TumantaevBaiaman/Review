import json

from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, permissions
from rest_framework.decorators import action, api_view, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .serializers import (
    CategoryListSerializer, CreateReviewOffice,
    CreateReviewKindergarten, CreateReviewSchool,
    PostSchoolSerializer, PostOfficeListSerializer,
    PostListCreate, CategoryListSerializerTest
)
from .models import (
    Category, Post,
    ReviewSchool, ReviewKindergarten,
    ReviewOffice,
)


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class ListCategory(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = CategoryListSerializerTest
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Category.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailCategory(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class ListPost(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = PostListCreate
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Post.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailPost(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Post.objects.all()
    serializer_class = PostListCreate

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class ListOffice(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = CreateReviewOffice
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = ReviewOffice.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailOffice(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = ReviewOffice.objects.all()
    serializer_class = CreateReviewOffice

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class ListSchool(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = CreateReviewSchool
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = ReviewSchool.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailSchool(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = ReviewSchool.objects.all()
    serializer_class = CreateReviewSchool

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)

class ListKindergarten(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = CreateReviewKindergarten
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = ReviewKindergarten.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailKindergarten(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = ReviewKindergarten.objects.all()
    serializer_class = CreateReviewKindergarten

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)

# #office
# class ListOffice(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     # authentication_classes = [SessionAuthentication]
#     serializer_class = PostOfficeListSerializer
#     passed_id = None
#
#     def get_queryset(self):
#         request = self.request
#         qs = Post.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, *args, **kwargs):
#         return self.create(*args, **kwargs)
#
#
# class DetailPost(
#     mixins.DestroyModelMixin,
#     mixins.UpdateModelMixin,
#     generics.RetrieveAPIView,
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin
# ):
#     permission_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostOfficeListSerializer
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['post_category']
#
#     def put(self, *args, **kwargs):
#         return self.update(*args, **kwargs)
#
#     def patch(self, *args, **kwargs):
#         return self.update(*args, **kwargs)





# class CategoryListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     # authentication_classes = [SessionAuthentication]
#     serializer_class = CategorySerializer
#     passed_id = None
#
#     def get_queryset(self):
#         request = self.request
#         qs = Category.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, *args, **kwargs):
#         return self.create(*args, **kwargs)
#
#
# class PostListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     # authentication_classes = [SessionAuthentication]
#     serializer_class = PostSerializer
#     passed_id = None
#
#     def get_queryset(self):
#         request = self.request
#         qs = Post.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, *args, **kwargs):
#         return self.create(*args, **kwargs)
#
#
# class PostDetailListAPIView(
#     mixins.DestroyModelMixin,
#     mixins.UpdateModelMixin,
#     generics.RetrieveAPIView,
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin
# ):
#     permission_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def put(self, *args, **kwargs):
#         return self.update(*args, **kwargs)
#
#     def patch(self, *args, **kwargs):
#         return self.update(*args, **kwargs)
