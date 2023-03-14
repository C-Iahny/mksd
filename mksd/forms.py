from django import forms 
from .models import Post, Category, Comment


#choices = [('sport', 'sport'), ('kultur', 'kultur')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title', 'author', 'category', 'body', 'snippet', 'header_image')

		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'Ihany', 'type': 'hidden'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
			'header_image': forms.FileInput(),

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










