# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='That guy', max_length=100),
        ),
    ]
