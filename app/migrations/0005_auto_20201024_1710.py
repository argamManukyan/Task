# Generated by Django 3.1.2 on 2020-10-24 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_userprofile_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='terms',
        ),
        migrations.AddField(
            model_name='terms',
            name='profile',
            field=models.ForeignKey(blank=True, default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user'),
            preserve_default=False,
        ),
    ]
