# Generated by Django 3.0.8 on 2020-08-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200803_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.SmallIntegerField(default=0),
        ),
    ]
