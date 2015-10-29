# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emiForms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='moreOptions',
            new_name='more_options',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='showImage',
            new_name='show_image',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='showTextHelp',
            new_name='show_text_help',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='timeQuestion',
            new_name='time_question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='typeQuestion',
            new_name='type_question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='textHelp',
        ),
        migrations.AddField(
            model_name='question',
            name='text_help',
            field=models.TextField(default=b'', max_length=300),
        ),
    ]
