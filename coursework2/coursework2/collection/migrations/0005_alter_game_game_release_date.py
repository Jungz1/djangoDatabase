# Generated by Django 3.2.7 on 2021-11-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_alter_console_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_release_date',
            field=models.DateField(verbose_name='date released'),
        ),
    ]
