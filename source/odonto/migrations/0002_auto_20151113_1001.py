# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('p01', models.CharField(max_length=4)),
                ('p01b', models.CharField(max_length=255)),
                ('p02', models.CharField(max_length=4)),
                ('p02b', models.CharField(max_length=255)),
                ('p03', models.CharField(max_length=4)),
                ('p03b', models.CharField(max_length=255)),
                ('p04', models.CharField(max_length=4)),
                ('p04b', models.CharField(max_length=255)),
                ('p05', models.CharField(max_length=4)),
                ('p06', models.CharField(max_length=4)),
                ('p07', models.CharField(max_length=4)),
                ('p08', models.CharField(max_length=4)),
                ('p09', models.CharField(max_length=4)),
                ('p10', models.CharField(max_length=4)),
                ('p11', models.CharField(max_length=4)),
                ('p12', models.CharField(max_length=4)),
                ('p13', models.CharField(max_length=4)),
                ('p14', models.CharField(max_length=4)),
                ('p14b', models.CharField(max_length=255)),
                ('p15', models.CharField(max_length=4)),
                ('p16', models.CharField(max_length=4)),
                ('p17', models.CharField(max_length=4)),
                ('p18', models.CharField(max_length=4)),
                ('p18b', models.CharField(max_length=255)),
                ('p19', models.CharField(max_length=4)),
                ('p19b', models.CharField(max_length=255)),
                ('p20', models.CharField(max_length=4)),
                ('p20b', models.CharField(max_length=255)),
                ('p21', models.CharField(max_length=4)),
                ('p21b', models.CharField(max_length=255)),
                ('p22', models.CharField(max_length=4)),
                ('p23', models.CharField(max_length=4)),
                ('p23b', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('CEP', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('tiposangue', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('rg', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('dataNascimento', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(to='odonto.User'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pessoa',
            field=models.OneToOneField(to='odonto.Pessoa'),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='user',
            field=models.OneToOneField(to='odonto.User'),
        ),
    ]
