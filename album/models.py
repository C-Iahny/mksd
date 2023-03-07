from django.db import models


class Album(models.Model):
	title = models.CharField(max_length=100)
	banner = models.ImageField(upload_to="album/banner")
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('album', args=[str(self.id)] )


class Images(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
	images = models.ImageField(upload_to="album/images")

	def __str__(self):
		return self.album.title


	#Pour fichier pdf mitmachen - ...
class FileUpload(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to="files/")
	file = models.FileField(upload_to="files/")


	def __str__(self):
		return self.name














