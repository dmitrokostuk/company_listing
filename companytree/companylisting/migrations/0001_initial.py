# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, unique=True)),
                ('company_estimated_earnings', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='companylisting.Genre')),
            ],
            options={
                'ordering': ['parent__id'],
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
