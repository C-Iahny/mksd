from django.contrib import admin
from django.urls import path, include

from .views import Add_Images, IndexView, AddCommentView, LikeView, CategoryListView, CategoryView, AddCategoryView, DeletePostView, UpdatePostView, AddPostView, ArticleDetailView, HomeView

urlpatterns = [


    path('', IndexView.as_view(), name="index"),
    path('all_post', HomeView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"), 
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"), 
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_images/', Add_Images.as_view(), name="add_images"),




]





