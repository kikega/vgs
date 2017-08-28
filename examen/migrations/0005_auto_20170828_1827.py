# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0004_auto_20170820_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oposicion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('oposicion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tema',
            name='oposicion',
            field=models.ManyToManyField(to='examen.Oposicion'),
        ),
    ]
