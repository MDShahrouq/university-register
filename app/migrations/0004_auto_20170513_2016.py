# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170513_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app.Professor')),
            ],
            options={
                'verbose_name_plural': 'courses',
                'verbose_name': 'course',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='app.Course'),
        ),
    ]
