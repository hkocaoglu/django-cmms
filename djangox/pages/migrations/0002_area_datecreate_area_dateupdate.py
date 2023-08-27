# Generated by Django 4.2 on 2023-08-24 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='dateCreate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='dateUpdate',
            field=models.DateField(auto_now=True),
        ),
    ]
