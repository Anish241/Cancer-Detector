# Generated by Django 4.1.7 on 2023-04-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_scan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
