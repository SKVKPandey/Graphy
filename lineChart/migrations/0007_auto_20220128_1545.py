# Generated by Django 3.2.10 on 2022-01-28 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineChart', '0006_auto_20220124_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t1score',
            name='Level',
        ),
        migrations.RemoveField(
            model_name='t2score',
            name='Level',
        ),
    ]
