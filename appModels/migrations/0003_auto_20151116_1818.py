# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appModels', '0002_equipos_img_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='goles',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='t_amarillas',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='t_rojas',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
