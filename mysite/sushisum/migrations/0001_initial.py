# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SushiPieces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sushi_tally', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SushiSitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sitting_date', models.DateTimeField(verbose_name=b'date of sitting')),
                ('location_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SushiType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_english', models.CharField(max_length=200)),
                ('name_japanese', models.CharField(max_length=200)),
                ('sushi_picture', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='sushipieces',
            name='sitting',
            field=models.ForeignKey(to='sushisum.SushiSitting'),
        ),
        migrations.AddField(
            model_name='sushipieces',
            name='sushi_type',
            field=models.ForeignKey(to='sushisum.SushiType'),
        ),
    ]
