from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add = False)
    updated = models.DateTimeField(auto_now=False,auto_now_add = True)

    def __unicode__(self): #__str__
        return self.email


class User(models.Model):
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Person(models.Model):
    user = models.OneToOneField(User)

    name = models.CharField(max_length=50)
    bloody_type = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    rg = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now= True)
    def __unicode__(self):
		return self.name

class Endereco(models.Model):
    person = models.OneToOneField(Person)

    street = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    CEP = models.CharField(max_length=50)

    def __unicode__(self):
        return self.street
