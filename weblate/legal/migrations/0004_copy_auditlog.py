# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 12:09
from __future__ import unicode_literals

from django.db import migrations


def copy_auditlog(apps, schema_editor):
    """Copy ipaddress and user agent information from the audit log."""
    Agreement = apps.get_model('legal', 'Agreement')
    for agreement in Agreement.objects.filter(address=None):
        try:
            log = agreement.user.auditlog_set.filter(
                activity='tos'
            ).order_by(
                '-timestamp'
            )[0]
        except IndexError:
            print 'NONE'
            continue

        agreement.address = log.address
        agreement.user_agent = log.user_agent
        agreement.save()


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0003_auto_20180416_1405'),
        ('accounts', '0036_auto_20180201_1059'),
    ]

    operations = [
        migrations.RunPython(copy_auditlog),
    ]