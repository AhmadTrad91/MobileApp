# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MobileApp', '0003_auto_20170907_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='agenda',
            table='Agenda',
        ),
        migrations.AlterModelTable(
            name='classes',
            table='Classes',
        ),
        migrations.AlterModelTable(
            name='course',
            table='Course',
        ),
        migrations.AlterModelTable(
            name='notifications',
            table='Notifications',
        ),
        migrations.AlterModelTable(
            name='section',
            table='Section',
        ),
    ]