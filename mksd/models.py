from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 
from ckeditor.fields import RichTextField



class Category(models.Model):
	name = models.CharField(max_length=255)
	img = models.ImageField(upload_to='cat_images/')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=[str(self.id)] )
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	biographie = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
	website_url = models.CharField(max_length=255, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)


	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	#title_tag = models.CharField(max_length=255, default="MKSD") tsy dia ilaina izy ito.
	header_image = models.ImageField(blank=True, null=True, upload_to="images")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	snippet = models.CharField(max_length=255, default='click the link above.')
	post_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255, default='MKSD Events')
	likes = models.ManyToManyField(User, related_name='mksd_event')
	images = models.ImageField(blank=True, null=True, upload_to="images/reglo_photo")
	file = models.FileField(upload_to="files/")

	def total_likes(self):
		return self.likes.count()


	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('article-detail', args=[str(self.id)] )


class Add_images(models.Model):
	images = models.ImageField(upload_to="images/cat_event")

	def __str__(self):
		return self.images 


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
















