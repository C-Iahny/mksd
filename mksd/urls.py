from django.contrib import admin
from django.urls import path, include

from .views import (
    AddNeuigkeitView,
    NeuigkeitDetail_list,
    NeuigkeitDetail,
    AddLiveView,
    AddMitmachen_indexView,
    MitList,
    MitDetail,
    uber_uns, 
    Unterstutzen, 
    Mitmachen,
    Mitmachen_index, 
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
    LiveList,
    LiveDetail,
    )

urlpatterns = [


    #OBJECTS VIEWS----------------------
    path('', IndexView, name="index"),
    path('all_post', HomeView.as_view(), name="home"),
    path('add_post/', AddPostView.as_view(), name="add_post"), 
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('mitmachen/', Mitmachen.as_view(), name='mitmachen'),
    path('neuigkeit_view/', NeuigkeitDetail_list.as_view(), name="neu_view"),
    path('live_list/', LiveList.as_view(), name='live_list'),
    path('mit_list/', MitList.as_view(), name='mit_list'),


    path('unterstutzen/', Unterstutzen, name='unterstutzen'),
    path('uber_uns/', uber_uns, name='uber_uns'),


    #OBJECTS DETAILS---------------------
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('neuigkeit_detail/<int:pk>/', NeuigkeitDetail.as_view(), name="neuigkeit_detail"),
    path('live_detail/<int:pk>', LiveDetail.as_view(), name='live_detail'),
    path('mit_detail/<int:pk>', MitDetail.as_view(), name='mit_detail'),




    #OBJECTS ADDITION---------------------
    path('add_category/', AddCategoryView.as_view(), name="add_category"), 
    path('add_images/', Add_Images.as_view(), name="add_images"),
    path('add_neuigkeit/', AddNeuigkeitView.as_view(), name='add_neuigkeit'),
    path('add_live/', AddLiveView.as_view(), name='add_live'),
    path('add_mitmachen_index/', AddMitmachen_indexView.as_view(), name='add_mitmachen_index'),




]





