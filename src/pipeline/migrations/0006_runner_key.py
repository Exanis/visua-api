# Generated by Django 2.0.6 on 2018-08-28 23:38

from django.db import migrations, models
import pipeline.models.runner


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0005_runner'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='key',
            field=models.CharField(default=pipeline.models.runner.make_secret_key, editable=False, max_length=32),
        ),
    ]
