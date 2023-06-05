from django import forms 
from .models import Post, Category, Comment, Add_images, Neuigkeit, Live, Mitmachen_index


#choices = [('sport', 'sport'), ('kultur', 'kultur')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title', 'author', 'category', 'body', 'snippet', 'header_image', 'file')

		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'Ihany', 'type': 'hidden'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
			'header_image': forms.FileInput(attrs={'class': 'form-control'}),
			#'file': forms.FileInput(attrs={'class': 'form-control'}),

		}


class Add_images(forms.ModelForm):
	class Meta:
		model = Add_images
		fields = ('images',)

		widgets = {
			'images': forms.FileInput(attrs={'class': 'form-control'}),
		}



class EditForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title', 'author', 'body', 'snippet', 'header_image')

		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
			'header_image': forms.FileInput(attrs={"rows": "", "class": "file_class_name"}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		} 


"""
neus = Neuigkeit.objects.all().values_list('name', 'name')

neus_list = []

for item in neus:
	neus_list.append(item)
"""

class NeuigkeitForm(forms.ModelForm):
	class Meta:
		model = Neuigkeit
		fields = ('title', 'body', 'image', 'file')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
			'file': forms.FileInput(attrs={'class': 'form-control'}),
			#'neu_date': forms.DateInput(attrs= {'class': 'datepicker'}, format= '%d/%m/%y'),
			#input_formats = ('%d/%m/%y')

		}

class LiveForm(forms.ModelForm):
	class Meta:
		model = Live
		fields = ('title', 'image', 'file', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
			'file': forms.FileInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

			#'neu_date': forms.FileInput(attrs={'class': 'form-control'}),
		}


class Mitmachen_indexForm(forms.ModelForm):
	class Meta:
		model = Mitmachen_index
		fields = ('title', 'image', 'file', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
			'file': forms.FileInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

			#'neu_date': forms.FileInput(attrs={'class': 'form-control'}),
		}





