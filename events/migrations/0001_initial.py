# Generated by Django 3.0.2 on 2020-01-31 16:19

import datetime
from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=20)),
                ('postalcode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=300)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date(2020, 1, 31))),
                ('fee', models.DecimalField(decimal_places=3, default=0, max_digits=1000)),
                ('max_capacity', models.PositiveSmallIntegerField()),
                ('min_capacity', models.PositiveSmallIntegerField(default=1)),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('OUT', 'Outdoor events'), ('GAM', 'Games')], max_length=3)),
            ],
        ),
    ]