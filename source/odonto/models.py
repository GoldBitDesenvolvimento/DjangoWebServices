from django.db import models
#models.ForeignKey(Publisher)
#models.ManyToManyField(Author)

# Create your models here.
class Endereco(models.Model):
    pessoa = models.OneToOneField(Pessoa)

    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    CEP = models.CharField(max_length=50)
    

class Pessoa(models.Model):
    usuario = models.OneToOneField(Usuario)

    nome = models.CharField(max_length=50)
    tiposangue = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    rg = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    
class Usuario(models.Model):
	pessoa = models.OneToOneField(Pessoa)

    usuario = models.CharField(max_length=50)
	senha = models.CharField(max_length=50)
	email = models.EmailField()
    

    def __unicode__(self):
        return self.email

# Create your models here.
class Anamnese(models.Model):
    usuario = models.OneToOneField(Usuario)

    p01 = models.CharField(max_length=4)
    p01b = models.CharField(max_length=255)
    p02 = models.CharField(max_length=4)
    p02b = models.CharField(max_length=255)
    p03 = models.CharField(max_length=4)
    p03b = models.CharField(max_length=255)
    p04 = models.CharField(max_length=4)
    p04b = models.CharField(max_length=255)
    p05 = models.CharField(max_length=4)
    p06 = models.CharField(max_length=4)
    p07 = models.CharField(max_length=4)
    p08 = models.CharField(max_length=4)
    p09 = models.CharField(max_length=4)
    p10 = models.CharField(max_length=4)
    p11 = models.CharField(max_length=4)
    p12 = models.CharField(max_length=4)
    p13 = models.CharField(max_length=4)
    p14 = models.CharField(max_length=4)
    p14b = models.CharField(max_length=255)
    p15 = models.CharField(max_length=4)
    p16 = models.CharField(max_length=4)
    p17 = models.CharField(max_length=4)
    p18 = models.CharField(max_length=4)
    p18b = models.CharField(max_length=255)
    p19 = models.CharField(max_length=4)
    p19b = models.CharField(max_length=255)
    p20 = models.CharField(max_length=4)
    p20b = models.CharField(max_length=255)
    p21 = models.CharField(max_length=4)
    p21b = models.CharField(max_length=255)
    p22 = models.CharField(max_length=4)
    p23 = models.CharField(max_length=4)
    p23b = models.CharField(max_length=255)
    
