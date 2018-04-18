# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from weblate.checks import CHECKS


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trans', '0130_auto_20180416_1503'),
        ('lang', '0011_auto_20180215_1158'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_hash', models.BigIntegerField()),
                ('check', models.CharField(choices=CHECKS.get_choices(), max_length=50)),
                ('ignore', models.BooleanField(db_index=True, default=False)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Project')),
            ],
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
