# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('capitulo', models.CharField(max_length=10)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Capitulos',
                'ordering': ['capitulo'],
                'verbose_name': 'Capitulo',
            },
        ),
        migrations.CreateModel(
            name='Errores',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pregunta', models.TextField(max_length=255, null=True)),
                ('correcta', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('acertadas', models.IntegerField()),
                ('erroneas', models.IntegerField()),
                ('nota', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pregunta', models.TextField(max_length=255)),
                ('res_a', models.TextField(max_length=255)),
                ('res_b', models.TextField(max_length=255)),
                ('res_c', models.TextField(max_length=255)),
                ('correcta', models.CharField(max_length=1)),
                ('capitulo', models.ForeignKey(to='examen.Capitulo')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tema', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'ordering': ['tema'],
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tema',
            field=models.ForeignKey(to='examen.Tema'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='tema',
            field=models.ForeignKey(to='examen.Tema'),
        ),
    ]
