from django.shortcuts import render
from .forms import ContactForm, UserForm
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.views.decorators.csrf import csrf_exempt 
from django.core import serializers
from django.http import HttpResponse

def home(request):
	
	title ="Wellcome"
	form = UserForm(request.POST or None)
	
	context = {
		"title":title,
		"form":form
	}

	if form.is_valid():
		#form.save()
		
		instance = form.save(commit=False)
		email = form.cleaned_data.get("email")
		instance.email = email
		if not instance.email:
			print "vazioo"	
		instance.save()
		context = {
			"title":"Thank you"
		}
	print request.POST

	
	return render(request,"home.html",context)
	
def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		'''	for key , value in form.cleaned_data.iteritems():
			print key , value
			#print form.cleaned_data.get(key)
		'''
		subject = 'contact form'
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_name = form.cleaned_data.get("full_name")
		#print email,message,full_name
		some_html_message = """
			<h1>hello</h1>
		"""
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s: %s via %s"%(
			form_name,
			form_message,
			form_email)
		

		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			html_message=some_html_message,
			fail_silently=False)
		
	context = {
		"form":form
	}
	return render(request,"forms.html",context)

@csrf_exempt 
def exemploPost(request):
	pessoa = ''
	
	if 'pessoa' in request.POST:
		pessoa = request.POST['pessoa']
		pessoa = Pessoa.objects.get(nome__contains = str(pessoa))	
	if pessoa == '':
		data = serializers.serialize("json", [])
	else:			
		data = serializers.serialize("json", [pessoa])
	
	return HttpResponse(data)


def getPaciente(request):
	pessoa = ''
	
	if 'id' in request.POST:
		pessoa = request.POST['id']
		pessoa = Pessoa.objects.get(pk = int(str(pessoa))	
	if pessoa == '':
		data = serializers.serialize("json", [])
	else:			
		data = serializers.serialize("json", [pessoa])
	
	return HttpResponse(data)

	