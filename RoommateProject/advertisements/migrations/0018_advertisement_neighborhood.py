# Generated by Django 5.0 on 2023-12-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0017_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='neighborhood',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]
