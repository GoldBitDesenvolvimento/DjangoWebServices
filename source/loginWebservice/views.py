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
		
		if not user :
			data = '[{"return": "invalid:User do not exits"}]'		
		else:			
			user_password = str(request.POST['password'])
			if user_password == user.get().password:
				data = serializers.serialize("json", [user.get()])
			else:
				data = '[{"return": "invalid:Password Erro"}]'	
	else:
		data = '[{"return": "invalid: Erro parameters on post"}]'	
	
	return HttpResponse(data)
@csrf_exempt 
def forgotPassword(request):	
	if 'email' in request.POST:
		user = User.objects.filter(email__contains = str(request.POST['email']))				
		if not user:
			data = '[{"return": "invalid:User do not exits"}]'		
		else:
			print 'Enviando para:'+user.get().email
			html_message= """
				<h1>Dados do Login</h1>
				<h2>Login:"""+user.get().email+"""</h2>
				<h2>Senha:"""+user.get().password+"""</h2>
				<img src="http://www.goldbit.com.br/imagens/logo.png" height="100" width="400">
			"""
			send_mail("Lembrar senha",
					"Senha para login:"+user.get().password,
					"contato@goldbit.com.br",
					[str(user.get().email)],
					html_message=html_message,
					fail_silently=False)
			data = '{"return": "Password:Send"}'	
	else:
		data = '[{"return": "invalid:User do not exits"}]'		
	
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



	