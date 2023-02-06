from django.db import models

# Create your models here.


class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	ville = models.CharField(max_length=100)
	subject = models.TextField(max_length=355)

	def __str__(self):
		return self.name


class Anmeldung(models.Model):
	team_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=25)
	name = models.CharField(max_length=100)
	stadt = models.CharField(max_length=100)
	text = models.TextField()

	def __str__(self):
		return self.team_name










