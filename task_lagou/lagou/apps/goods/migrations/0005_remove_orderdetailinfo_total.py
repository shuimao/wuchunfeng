# Generated by Django 2.2.3 on 2019-07-19 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_remove_orderinfo_oid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetailinfo',
            name='total',
        ),
    ]