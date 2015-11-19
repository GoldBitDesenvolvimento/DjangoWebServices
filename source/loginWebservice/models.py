from django.db import models

# Create your models here.



class User(models.Model):
    password = models.CharField(max_length=50)
    email = models.EmailField()
    def __unicode__(self): #__str__
        return self.email

class Person(models.Model):
    user = models.OneToOneField(User)
    address = models.OneToOneField(Address)
    name = models.CharField(max_length=50)
    bloody_type = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    rg = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now= True)
    def __unicode__(self):
		return self.name

class Address(models.Model):
    street = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    CEP = models.CharField(max_length=50)

    def __unicode__(self):
        return self.street
