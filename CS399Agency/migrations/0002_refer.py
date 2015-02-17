# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CS399Agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('fEmail', models.EmailField(max_length=254)),
                ('fFirstName', models.CharField(default=b'', max_length=128)),
                ('fLastName', models.CharField(default=b'', max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
