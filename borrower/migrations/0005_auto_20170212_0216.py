# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrower', '0004_auto_20170212_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]