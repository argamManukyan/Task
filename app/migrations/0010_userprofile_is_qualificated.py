# Generated by Django 3.1.2 on 2020-10-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201024_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_qualificated',
            field=models.BooleanField(default=False),
        ),
    ]