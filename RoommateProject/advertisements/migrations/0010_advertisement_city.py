# Generated by Django 5.0 on 2023-12-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0009_remove_advertisement_city_delete_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'Riyadh')], default=2, max_length=500),
            preserve_default=False,
        ),
    ]
