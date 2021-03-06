# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-11 18:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=13)),
                ('address1', models.CharField(max_length=75)),
                ('town', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=8)),
                ('country', models.CharField(choices=[('UK', 'United Kingdom'), ('US', 'United States of America'), ('IR', 'Ireland'), ('SC', 'Scotland'), ('WA', 'Wales')], default='UK', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]
