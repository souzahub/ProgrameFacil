# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_movrotativo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movrotativo',
            old_name='veiuclo',
            new_name='veiculo',
        ),
    ]