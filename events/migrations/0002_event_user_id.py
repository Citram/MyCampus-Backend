# Generated by Django 3.0.3 on 2020-03-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
