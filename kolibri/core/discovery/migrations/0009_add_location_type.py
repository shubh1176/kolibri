# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-08-08 17:45
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("discovery", "0008_networklocation_is_local"),
    ]

    operations = [
        migrations.AddField(
            model_name="networklocation",
            name="location_type",
            field=models.CharField(
                choices=[
                    ("Dynamic", "dynamic"),
                    ("Reserved", "reserved"),
                    ("Static", "static"),
                ],
                default="static",
                max_length=8,
            ),
        ),
    ]