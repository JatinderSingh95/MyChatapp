# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-30 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0029_profile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='codd',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]