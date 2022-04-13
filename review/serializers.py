from tkinter import Image

from django.urls import reverse
from django.utils.timezone import now
from rest_framework import serializers
from .models import (
    ReviewSchool, ReviewKindergarten,
    ReviewOffice, Post,
    Category
)


class ImageSerializer(serializers.ModelSerializer):
    #max 50 images
    class Meta:
        model = Image
        fields = (
            # 'account_id',
            'images',
        )


#create
class CreateReviewSchool(serializers.ModelSerializer):

    class Meta:
        model = ReviewSchool
        fields = [
            'review_post', 'review',
            'purity', 'nutrition', 'training_program',
            'security', 'locations', 'office', 'quality_of_education',
            'price_and_quality', 'study_guides', 'rating_average',
        ]


class CreateReviewOffice(serializers.ModelSerializer):

    class Meta:
        model = ReviewOffice
        fields = [
            'review_post', 'review',
            'reputation', 'staff', 'support', 'accompany',
            'efficiency', 'price_and_quality', 'rating_average'
        ]


class CreateReviewKindergarten(serializers.ModelSerializer):
    class Meta:
        model = ReviewKindergarten
        fields = [
            'review_post', 'review',
            'purity', 'nutrition', 'activity', 'upbringing',
            'security', 'locations', 'office', 'baby_care',
            'price_and_quality', 'rating_average'
        ]


class PostListCreate(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'post_category', 'name_post', 'content'
        ]


#list
class PostList(serializers.ModelSerializer):
    review_office = CreateReviewOffice(many=True)
    review_school = CreateReviewSchool(many=True)
    review_cat_kindergarten = CreateReviewKindergarten(many=True)

    class Meta:
        model = Post
        fields = [
            'post_category', 'name_post', 'content', 'review_office', 'review_school', 'review_cat_kindergarten'
        ]

        for i in fields:
            print(Post.objects.values(i))



class CategoryListSerializer(serializers.ModelSerializer):
    url_category = serializers.SerializerMethodField(read_only=True)
    cat = PostList(many=True)

    def get_url_category(self, obj):
        return "http://127.0.0.1:8000/category/{id}".format(id=obj.id)

    class Meta:
        model = Category
        fields = [
            'name_category', 'update', 'timestamp', 'url_category', 'cat'
        ]


class PostListTest(serializers.ModelSerializer):
    # review_office = CreateReviewOffice(many=True)
    # review_school = CreateReviewSchool(many=True)
    # review_cat_kindergarten = CreateReviewKindergarten(many=True)

    class Meta:
        model = Post
        fields = [
            'post_category', 'name_post', 'content'
        ]

        for i in fields:
            print(Post.objects.values(i))


class CategoryListSerializerTest(serializers.ModelSerializer):
    url_category = serializers.SerializerMethodField(read_only=True)

    def get_url_category(self, obj):
        return "http://127.0.0.1:8000/category/{id}".format(id=obj.id)

    class Meta:
        model = Category
        fields = [
            'name_category', 'update', 'timestamp', 'url_category'
        ]


class PostOfficeListSerializer(serializers.ModelSerializer):
    # review_office = CreateReviewOffice(many=True)

    class Meta:
        model = Post
        fields = [
            'post_category', 'name_post', 'content',
        ]


class PostSchoolSerializer(serializers.ModelSerializer):
    review_school = CreateReviewSchool(many=True)

    class Meta:
        model = Post
        fields = [
            'post_category', 'name_post', 'content', 'review_school'
        ]












