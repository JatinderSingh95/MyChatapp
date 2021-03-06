# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0023_auto_20170810_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='createclass',
            name='Image',
            field=models.ImageField(blank=True, upload_to=b'profile_image'),
        ),
        migrations.AlterField(
            model_name='createclass',
            name='From',
            field=models.CharField(choices=[(b'01:00 am', b'01:00 am'), (b'02:00 am', b'02:00 am'), (b'03:00 am', b'03:00 am'), (b'04:15 am', b'04:00 am'), (b'05:00 am', b'05:00 am'), (b'06:00 am', b'06:00 am'), (b'07:00 am', b'07:00 am'), (b'08:00 am', b'08:00 am'), (b'09:00 am', b'09:00 am'), (b'10:00 am', b'10:00 am'), (b'11:00 am', b'11:00 am'), (b'12:00 am', b'12:00 am'), (b'01:00 pm', b'01:00 pm'), (b'02:00 pm', b'02:00 pm'), (b'03:00 pm', b'03:00 pm'), (b'04:00 pm', b'04:00 pm'), (b'05:00 pm', b'05:00 pm'), (b'06:00 pm', b'06:00 pm'), (b'07:00 pm', b'07:00 pm'), (b'08:00 pm', b'08:00 pm'), (b'09:00 pm', b'09:00 pm'), (b'10:00 pm', b'10:00 pm'), (b'11:00 pm', b'11:00 pm'), (b'12:00 pm', b'12:00 pm')], default=b'', max_length=60),
        ),
        migrations.AlterField(
            model_name='createclass',
            name='to',
            field=models.CharField(choices=[(b'01:00 am', b'01:00 am'), (b'02:00 am', b'02:00 am'), (b'03:00 am', b'03:00 am'), (b'04:00 am', b'04:00 am'), (b'05:00 am', b'05:00 am'), (b'06:00 am', b'06:00 am'), (b'07:00 am', b'07:00 am'), (b'08:00 am', b'08:00 am'), (b'09:00 am', b'09:00 am'), (b'10:00 am', b'10:00 am'), (b'11:00 am', b'11:00 am'), (b'12:00 am', b'12:00 am'), (b'01:00 pm', b'01:00 pm'), (b'02:00 pm', b'02:00 pm'), (b'03:00 pm', b'03:00 pm'), (b'04:00 pm', b'04:00 pm'), (b'05:00 pm', b'05:00 pm'), (b'06:00 pm', b'06:00 pm'), (b'07:00 pm', b'07:00 pm'), (b'08:00 pm', b'08:00 pm'), (b'09:00 pm', b'09:00 pm'), (b'10:00 pm', b'10:00 pm'), (b'11:00 pm', b'11:00 pm'), (b'12:00 pm', b'12:00 pm')], default=b'', max_length=60),
        ),
    ]
