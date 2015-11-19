# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=50)),
                ('neighborhood', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('CEP', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('bloody_type', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('rg', models.CharField(max_length=50)),
                ('cellphone', models.CharField(max_length=50)),
                ('home_phone', models.CharField(max_length=50)),
                ('birth_date', models.DateField(auto_now=True)),
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
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(to='loginWebservice.User'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='person',
            field=models.OneToOneField(to='loginWebservice.Person'),
        ),
    ]
