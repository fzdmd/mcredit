# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borrower', '0008_remove_borrower_contacts'),
        ('main', '0003_auto_20170212_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='borrower.Borrower'),
        ),
    ]