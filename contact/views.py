from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Contact, Anmeldung
from django.core.mail import send_mail




# Create your views here.


def Kontact(request):

	if request.method == 'POST':
		contact = Contact()
		message_name 	= request.POST.get('name')
		from_email 		= request.POST.get('from-email')
		ville 			= request.POST.get('stadt')
		message 		= request.POST.get('text')

		contact.name = message_name 
		contact.email = from_email
		ville 			= ville
		contact.subject = message  

		contact.save()

		message = f"""  

		Name: {message_name}
		From: {from_email}
		Stadt: {ville}

		New message: \n\n{message}

		"""

		# Send email
		send_mail(
			message_name, #subject
			message, #message
			from_email, #from email
			['kontakt.mksd@gmail.com'], #to email
			fail_silently=False, 

			)


		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})



class About(TemplateView):
	model = Contact
	template_name = 'about.html'


class Impressum(TemplateView):
	model = Contact
	template_name = 'impressum.html'



# Anmeldung -------------------------------------------------------------------

def Anmeldebogen(request):

	if request.method == 'POST':
		anmeldung 	= Anmeldung()
		team_name 	= request.POST.get('team-name')
		from_email 	= request.POST.get('from-email')
		phone 	= request.POST.get('phone')
		name 		= request.POST.get('name')
		stadt 		= request.POST.get('stadt')
		text 		= request.POST.get('text')

		anmeldung.team_name = team_name 
		anmeldung.email 	= from_email
		anmeldung.phone 	= phone
		anmeldung.name 		= name
		anmeldung.stadt 	= stadt
		anmeldung.text 		= text  

		anmeldung.save()

		text = f"""  

		Name: {name}
		From: {from_email}
		Stadt: {stadt}
		Phone: {phone}
		Team name: {team_name}

		New message: \n\n{text}

		"""
		

		# Send email
		send_mail(
			team_name, #subject
			text, #message
			from_email, #from email
			['anmeldung.mksd@gmail.com'], #to email
			fail_silently=False, 

			)


		return render(request, 'anmeldebogen.html', {'text': text})

	else:
		return render(request, 'anmeldebogen.html', {})


def Faq(request):
	context = {}
	return render(request, 'faq.html', context)
