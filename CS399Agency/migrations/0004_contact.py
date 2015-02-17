# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CS399Agency', '0003_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('firstName', models.CharField(default=b'', max_length=128)),
                ('lastName', models.CharField(default=b'', max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(default=b'', max_length=128)),
                ('message', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
