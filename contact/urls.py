from django.urls import path
from .views import Kontact, About, Impressum, Anmeldebogen, Faq



urlpatterns = [
	path('contact/', Kontact, name="contact"), 
	path('about/', About.as_view(), name="about"), 
	path('impressum/', Impressum.as_view(), name="impressum"), 
	path('anmeldebogen/', Anmeldebogen, name="anmeldebogen"), 
	path('faq/', views.Faq, name="faq"),


]
