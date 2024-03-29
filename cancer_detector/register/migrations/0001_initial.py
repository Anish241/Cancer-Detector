# Generated by Django 4.1.7 on 2023-03-28 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('registration_number', models.CharField(blank=True, max_length=100)),
                ('specialization', models.CharField(blank=True, max_length=100)),
                ('hospital_name', models.CharField(blank=True, max_length=100)),
                ('hospital_address', models.CharField(blank=True, max_length=100)),
                ('hospital_phone', models.CharField(blank=True, max_length=100)),
                ('hospital_email', models.EmailField(blank=True, max_length=100)),
                ('hospital_pincode', models.CharField(blank=True, max_length=100)),
                ('hospital_city', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
