from django.db import models
#models.ForeignKey(Publisher)
#models.ManyToManyField(Author)

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add = False)
    updated = models.DateTimeField(auto_now=False,auto_now_add = True)

    def __unicode__(self): #__str__
        return self.email


class User(models.Model):
    #user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    
class Pessoa(models.Model):
    user = models.OneToOneField(User)

    nome = models.CharField(max_length=50)
    tiposangue = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    rg = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    dataNascimento = models.DateField(auto_now= True)
    
class Endereco(models.Model):
    pessoa = models.OneToOneField(Pessoa)

    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    CEP = models.CharField(max_length=50)
    def __unicode__(self):
        return self.email

# Create your models here.
class Anamnese(models.Model):
    user = models.OneToOneField(User)
    date = models.DateField(auto_now=True,auto_now_add = False)
    p01 = models.CharField(max_length=4)
    p01b = models.CharField(max_length=255,default='NULL')
    p02 = models.CharField(max_length=4, default='NULL')
    p02b = models.CharField(max_length=255, default='NULL')
    p03 = models.CharField(max_length=4, default='NULL')
    p03b = models.CharField(max_length=255, default='NULL')
    p04 = models.CharField(max_length=4, default='NULL')
    p04b = models.CharField(max_length=255, default='NULL')
    p05 = models.CharField(max_length=4, default='NULL')
    p06 = models.CharField(max_length=4, default='NULL')
    p07 = models.CharField(max_length=4, default='NULL')
    p08 = models.CharField(max_length=4, default='NULL')
    p09 = models.CharField(max_length=4, default='NULL')
    p10 = models.CharField(max_length=4, default='NULL')
    p11 = models.CharField(max_length=4, default='NULL')
    p12 = models.CharField(max_length=4, default='NULL')
    p13 = models.CharField(max_length=4, default='NULL')
    p14 = models.CharField(max_length=4, default='NULL')
    p14b = models.CharField(max_length=255, default='NULL')
    p15 = models.CharField(max_length=4, default='NULL')
    p16 = models.CharField(max_length=4, default='NULL')
    p17 = models.CharField(max_length=4, default='NULL')
    p18 = models.CharField(max_length=4, default='NULL')
    p18b = models.CharField(max_length=255, default='NULL')
    p19 = models.CharField(max_length=4, default='NULL')
    p19b = models.CharField(max_length=255, default='NULL')
    p20 = models.CharField(max_length=4, default='NULL')
    p20b = models.CharField(max_length=255, default='NULL')
    p21 = models.CharField(max_length=4, default='NULL')
    p21b = models.CharField(max_length=255, default='NULL')
    p22 = models.CharField(max_length=4, default='NULL')
    p23 = models.CharField(max_length=4, default='NULL')
    p23b = models.CharField(max_length=255, default='NULL')
    
