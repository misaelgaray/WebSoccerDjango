# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_equipo', models.CharField(max_length=50)),
                ('puntos', models.IntegerField()),
                ('p_jugados', models.IntegerField()),
                ('p_ganados', models.IntegerField()),
                ('p_empatados', models.IntegerField()),
                ('p_perdidos', models.IntegerField()),
                ('goles_totales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_jugador', models.CharField(max_length=50)),
                ('posicion', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('goles', models.IntegerField()),
                ('t_amarillas', models.IntegerField()),
                ('t_rojas', models.IntegerField()),
                ('id_equipo', models.ForeignKey(to='appModels.Equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_jugador', models.ForeignKey(to='appModels.Jugador')),
            ],
        ),
    ]
