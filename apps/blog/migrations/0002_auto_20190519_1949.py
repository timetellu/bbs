# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-19 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='nid',
            new_name='id',
        ),
    ]
