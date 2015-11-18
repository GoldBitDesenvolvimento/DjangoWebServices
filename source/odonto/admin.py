from django.contrib import admin
#from .forms import SignUpForm
from .models import SignUp
from .models import *
# Register your models here.

'''
class SignUpAdmin(admin.modelAdmin):
	list_display = ["__unicode__","timestamp","updated"
	#cmform = SignUpForm
	#class Meta:
	#	model = Sign
'''

#admin.site.register(SignUp,SignUpAdmin)
admin.site.register(User)
admin.site.register(Pessoa)