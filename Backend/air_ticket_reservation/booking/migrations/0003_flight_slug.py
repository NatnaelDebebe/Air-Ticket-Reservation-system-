# Generated by Django 5.0.6 on 2024-08-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='slug',
            field=models.SlugField(default='-'),
            preserve_default=False,
        ),
    ]
