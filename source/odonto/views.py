from django.shortcuts import render
from .forms import ContactForm ,UserForm

# Create your views here.


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
		for key , value in form.cleaned_data.iteritems():
			print key , value
			#print form.cleaned_data.get(key)
		'''
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		print email,message,full_name
'''
		
	context = {
		"form":form
	}
	return render(request,"forms.html",context)


def getPaciente(request):
	if request.method == "POST":
		print request.POST
		print 'sddddddd'
		request.POST['email']
	
	
	print "aeee"
	return render(request,"home.html",context)

	