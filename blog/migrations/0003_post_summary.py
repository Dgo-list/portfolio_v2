# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]