# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address_city',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address_state',
            field=models.CharField(max_length=2, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address_street',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address_zip',
            field=models.IntegerField(max_length=5, null=True),
            preserve_default=True,
        ),
    ]
