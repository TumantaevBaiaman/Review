from django.urls import path
from .views import (
    ListCategory, DetailCategory, ListPost,
    ListOffice, DetailOffice,
    ListSchool, DetailSchool,
    ListKindergarten, DetailKindergarten, DetailPost
)


urlpatterns = [
    path('category/', ListCategory.as_view(), name='category'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='detail_category'),
    path('post/', ListPost.as_view(), name='post'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
    path('office/', ListOffice.as_view(), name='office'),
    path('office/<int:pk>/', DetailOffice.as_view(), name='detail_office'),
    path('school/', ListSchool.as_view(), name='school'),
    path('school/<int:pk>/', DetailSchool.as_view(), name='detail_school'),
    path('kindergarten/', ListKindergarten.as_view(), name='kindergarten'),
    path('kindergarten/<int:pk>/', DetailKindergarten.as_view(), name='detail_kindergarten'),
]