from django import forms
from .models import User

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.CharField()
	message = forms.CharField()


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email','password']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		return email

	def clean_password(self):
		return self.cleaned_data.get('password')
		

