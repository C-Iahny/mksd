from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Album, Images, FileUpload
from .forms import AlbumForm, EditAlbumForm
from django.urls import reverse_lazy



class AlbumView(TemplateView):
	model = Album
	template_name = "albums.html"
	ordering = ['-album.id', 'url']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['album_list'] = Album.objects.all()
		return context


# add product
class CreateAlbumView(CreateView):
	template_name = "add_album.html"
	form_class = AlbumForm 
	success_url = reverse_lazy("album")


# Product detail
class AlbumDetailView(TemplateView):
	model = Album
	template_name = "album_detail.html"
	ordering = ['-id']

	def get_context_data(self, **kwargs):
		context = super(AlbumDetailView, self).get_context_data(**kwargs)
		context ['album_obj'] = Album.objects.get(id = self.kwargs['pk'])

		return context


class UpdateAlbumView(UpdateView):
	model = Album 
	template_name = 'update_album.html'
	form_class = EditAlbumForm

	success_url = reverse_lazy('album')

class DeleteAlbumView(DeleteView):
	model = Album
	template_name = 'delete_album.html'

	success_url = reverse_lazy('album')


# Add product images
class AddAlbumImages(TemplateView):
	template_name = "addimages.html"

	def post(self, *args, **kwargs):
		try:
			images = self.request.FILES.getlist('images')
			album = Album.objects.get(id = self.kwargs['pk'])

			for image in images:
				product_images = Images.objects.create(
						album = album,
						images = image

					)
			return redirect('album')
		except ValueError as e:
			print(e)
		except Album.DoesNotExist as e:
			print(e)


# Image Details
class ImgaeDetail(TemplateView):
	model = Images
	template_name = 'imagedetail.html'
	ordering = ['-id']



def Files_Upload(request):
	files_post = FileUpload.objects.all()
	return render(request, 'mitmachen.html', {'files_post': files_post})


class AddFiles(CreateView):
	model = FileUpload
	template_name = "addfiles.html"
	fields = '__all__' 
	success_url = reverse_lazy("file_upload")











