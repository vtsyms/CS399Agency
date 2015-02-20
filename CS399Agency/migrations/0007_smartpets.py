# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CS399Agency', '0006_auto_20150219_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartpets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
