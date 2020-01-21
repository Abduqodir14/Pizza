# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='favourite_pizza',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='pizza_app.PizzaMenuItem'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='our_note',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]
