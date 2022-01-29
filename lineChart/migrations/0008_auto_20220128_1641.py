# Generated by Django 3.2.10 on 2022-01-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineChart', '0007_auto_20220128_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.IntegerField()),
                ('team2', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='T1Score',
        ),
        migrations.DeleteModel(
            name='T2Score',
        ),
    ]