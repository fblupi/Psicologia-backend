# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(default=b'', max_length=100, blank=True)),
                ('image', models.ImageField(default=b'', upload_to=b'Form/')),
                ('theme', models.TextField(default=b'', max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=300)),
                ('type_question', models.IntegerField()),
                ('show_text_help', models.BooleanField(default=False)),
                ('text_help', models.TextField(default=b'', max_length=300)),
                ('values', models.TextField()),
                ('show_image', models.BooleanField(default=False)),
                ('image', models.TextField(default=b'')),
                ('required', models.BooleanField(default=False)),
                ('time_question', models.IntegerField(default=0)),
                ('more_options', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
                ('form', models.ForeignKey(default=0, to='emiForms.Form')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
