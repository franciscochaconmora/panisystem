# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0001_initial'),
    ]

    operations = [
      migrations.RenameField('Indicador','pub_data','fecha_publicacion'),
    ]
