# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=250)),
                ('description', models.CharField(default=b'', max_length=500)),
                ('link', models.CharField(default=b'', max_length=600, blank=True)),
                ('gifted', models.BooleanField(default=False)),
                ('rank', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_city', models.CharField(max_length=200)),
                ('address_state', models.CharField(max_length=2)),
                ('address_street', models.CharField(max_length=200)),
                ('address_zip', models.IntegerField(max_length=5)),
                ('user', models.OneToOneField(related_name='info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
