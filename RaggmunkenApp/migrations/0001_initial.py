# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servingdate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='username',
            field=models.ForeignKey(to='RaggmunkenApp.User'),
        ),
        migrations.AddField(
            model_name='alertlist',
            name='fooditem',
            field=models.ForeignKey(to='RaggmunkenApp.FoodItem'),
        ),
    ]
