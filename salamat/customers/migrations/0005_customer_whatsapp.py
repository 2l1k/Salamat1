# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20180904_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='whatsapp',
            field=models.CharField(max_length=30, null=True, verbose_name='Whatsapp', blank=True),
        ),
    ]
