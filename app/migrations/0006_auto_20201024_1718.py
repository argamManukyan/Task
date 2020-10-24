# Generated by Django 3.1.2 on 2020-10-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201024_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terms',
            name='profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='terms',
            field=models.ManyToManyField(related_name='terms', to='app.Terms'),
        ),
    ]
