from django.urls import path
from .views import DeleteAlbumView, UpdateAlbumView, AddFiles, Files_Upload, AlbumView, CreateAlbumView, AlbumDetailView, AddAlbumImages, ImgaeDetail




urlpatterns = [

	path('album/', AlbumView.as_view(), name="album"),
	path('add_album/', CreateAlbumView.as_view(), name="add_album"),
	path('album_detail/<int:pk>/', AlbumDetailView.as_view(), name="album_detail"),
	path('addimages/<int:pk>/', AddAlbumImages.as_view(), name="addimages"),
	path('imagedetail/<int:pk>/', ImgaeDetail.as_view(), name="imagedetail"),
	path('file_upload/', Files_Upload, name='file_upload'),
	path('addfiles/', AddFiles.as_view(), name='addfiles'),
    path('album/edit/<int:pk>', UpdateAlbumView.as_view(), name="update_album"),
    path('album/<int:pk>/remove', DeleteAlbumView.as_view(), name="delete_album"),




]










