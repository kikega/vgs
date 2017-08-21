# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0003_auto_20170820_2049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examen',
            options={'verbose_name_plural': 'Examenes'},
        ),
    ]
