# Generated by Django 3.2.10 on 2022-01-24 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineChart', '0003_auto_20220124_1444'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='T2Point',
            new_name='T1Points',
        ),
        migrations.RenameModel(
            old_name='T1Point',
            new_name='T2Points',
        ),
    ]