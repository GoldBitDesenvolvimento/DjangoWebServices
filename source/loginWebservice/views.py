from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from loginWebservice.models import User
from django.views.decorators.csrf import csrf_exempt 
from django.core import serializers
from django.http import HttpResponse


@csrf_exempt 
def getLoginWebservice(request):
	user = ''	
	if 'email' in request.POST and 'password' in request.POST:
		user = User.objects.filter(email__contains = str(request.POST['email']))
		print str(user.email)

		'''
		if user == '':
			data = serializers.serialize("json", [])
		else:			
			user_password = str(request.POST['password'])
			print str(user.email)
			data = 'ok'#serializers.serialize("json", [user])
			if user_password == user.get('password'):
				data = serializers.serialize("json", [])
				print 'aeee'
			else:
				data = serializers.serialize("json", [])	
			data = serializers.serialize("json", [])
	else:
		data = serializers.serialize("json", [])
	'''
	data = serializers.serialize("json", user)
	return HttpResponse(data)

# Create your views here.
@csrf_exempt 
def getPaciente(request):
	pessoa = ''
	
	if 'id' in request.POST:
		pessoa = request.POST['id']
		pessoa = Pessoa.objects.get(pk = int(str(pessoa)))	
	if pessoa == '':
		data = serializers.serialize("json", [])
	else:			
		data = serializers.serialize("json", [pessoa])
	
	return HttpResponse(data)



	