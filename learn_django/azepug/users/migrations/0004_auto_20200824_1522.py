# Generated by Django 3.0.8 on 2020-08-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Barəmdə'),
        ),
    ]
