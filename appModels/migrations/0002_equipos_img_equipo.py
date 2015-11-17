# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import appModels.models


class Migration(migrations.Migration):

    dependencies = [
        ('appModels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='img_equipo',
            field=models.FileField(null=True, upload_to=appModels.models.get_upload_file_name, blank=True),
        ),
    ]
