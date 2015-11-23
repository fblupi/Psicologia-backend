# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('values', models.TextField(blank=True)),
                ('time', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.CharField(default=b'', max_length=2000, blank=True)),
                ('image', models.ImageField(default=b'', upload_to=b'Form/')),
                ('theme', models.TextField(default=b'', max_length=100)),
                ('time', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FormEnabled',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=False)),
                ('max_answer', models.IntegerField(default=1)),
                ('auth', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accounts', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=300, blank=True)),
                ('type_question', models.IntegerField()),
                ('show_text_help', models.BooleanField(default=False)),
                ('text_help', models.TextField(default=b'', max_length=300)),
                ('values', models.TextField(blank=True)),
                ('values_number', models.TextField(default=0, blank=True)),
                ('show_image', models.BooleanField(default=False)),
                ('image', models.ImageField(default=b'', upload_to=b'Question/')),
                ('required', models.BooleanField(default=False)),
                ('time_question', models.IntegerField(default=0)),
                ('more_options', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('form', models.ForeignKey(default=0, to='emiForms.Form')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SendListModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('period', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('list', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='form',
            name='form_enabled',
            field=models.OneToOneField(to='emiForms.FormEnabled'),
        ),
        migrations.AddField(
            model_name='form',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='form',
            field=models.ForeignKey(to='emiForms.Form'),
        ),
        migrations.AddField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
