from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album 
		fields = '__all__'
		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
			'display_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Select banner image'})

		}



class EditAlbumForm(forms.ModelForm):
	class Meta:
		model = Album 
		fields = '__all__'
		widgets = {

			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
			'display_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Select banner image'})

		}



