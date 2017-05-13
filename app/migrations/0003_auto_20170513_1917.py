# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=64, verbose_name='first name')),
                ('last_name', models.CharField(max_length=64, verbose_name='last name')),
                ('dni', models.CharField(max_length=64, verbose_name='student ID')),
                ('profession', models.CharField(max_length=64, verbose_name='profession')),
            ],
            options={
                'verbose_name_plural': 'professors',
                'verbose_name': 'professor',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'university', 'verbose_name_plural': 'universities'},
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='professor',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professors', to='app.University'),
        ),
    ]