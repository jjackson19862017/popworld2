# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-12 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('original_item_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('instant_buy_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('reserved_buy_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('image', models.ImageField(height_field='height_field', upload_to='images', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('series', models.CharField(default='', max_length=200)),
                ('character', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
