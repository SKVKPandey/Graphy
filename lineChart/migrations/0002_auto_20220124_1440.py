# Generated by Django 3.2.10 on 2022-01-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineChart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Level', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Team',
            new_name='Team1',
        ),
        migrations.RenameField(
            model_name='team1',
            old_name='data',
            new_name='Level',
        ),
    ]
