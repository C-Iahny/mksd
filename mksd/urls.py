from django.contrib import admin
from django.urls import path, include

from .views import (
    AddNeuigkeitView,
    AddLiveView,
    AddMitmachen_indexView,
    uber_uns, 
    Unterstutzen, 
    Mitmachen, 
    Add_Images, 
    IndexView, 
    AddCommentView, 
    LikeView, 
    CategoryListView, 
    CategoryView, 
    AddCategoryView, 
    DeletePostView, 
    UpdatePostView, 
    AddPostView, 
    ArticleDetailView, 
    HomeView,
    )

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
    path('mitmachen/', Mitmachen.as_view(), name='mitmachen'),
    path('unterstutzen/', Unterstutzen, name='unterstutzen'),
    path('uber_uns/', uber_uns, name='uber_uns'),
    path('add_neuigkeit/', AddNeuigkeitView.as_view(), name='add_neuigkeit'),
    path('add_live/', AddLiveView.as_view(), name='add_live'),
    path('add_mitmachen_index/', AddMitmachen_indexView.as_view(), name='add_mitmachen_index'),




]





