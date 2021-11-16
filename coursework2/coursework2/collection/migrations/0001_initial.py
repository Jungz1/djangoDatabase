# Generated by Django 3.2.9 on 2021-11-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('console_name', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('price', models.IntegerField()),
                ('developer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=200)),
                ('game_release_date', models.DateTimeField(verbose_name='date released')),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('compatible_consoles', models.ManyToManyField(to='collection.Console')),
            ],
        ),
    ]
