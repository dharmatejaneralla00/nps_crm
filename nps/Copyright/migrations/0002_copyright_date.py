# Generated by Django 4.1.1 on 2023-02-04 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Copyright', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='copyright',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
