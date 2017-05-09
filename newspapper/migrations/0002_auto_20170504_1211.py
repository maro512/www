# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 12:11
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newspapper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 5, 4, 12, 11, 25, 104631, tzinfo=utc))),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='is_confirmed',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='article',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 5, 4, 12, 11, 25, 73904, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspapper.Article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]