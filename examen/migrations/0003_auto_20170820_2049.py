# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0002_tema_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'ordering': ['tema'], 'verbose_name_plural': 'Temas'},
        ),
    ]
